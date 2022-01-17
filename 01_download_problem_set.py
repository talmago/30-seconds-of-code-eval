import argparse
import logging
import os
import shutil
import subprocess
import marko
import tqdm
import srsly

from bs4 import BeautifulSoup
from more_itertools import split_before

LOG = logging.getLogger(__name__)


def download_repo(repo_url, output_dir=None, clone_timeout=150):
    """Download a repository from Github into local file system.
    Clone only a single branch with no history (tree depth = 1).
    Use ``clone_timeout`` to limit the time of the operation.

    Args:
        repo_url (str): repo url.
        output_dir (str): optional, output directory (default is '.tmp/<REPO_NAME>').
        clone_timeout (int): optional, timeout in seconds. default is 150.

    Returns:
        str, repo dir.
    """
    repo_name = repo_url.split("/")[-1]
    output_dir = output_dir or "./.tmp"
    repo_dir = os.path.join(output_dir, repo_name)

    p = subprocess.Popen(
        f"GIT_TERMINAL_PROMPT=0 git clone --depth 1 --single-branch {repo_url} {repo_dir}",
        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
    )

    try:
        p.wait(clone_timeout)
    except subprocess.TimeoutExpired:
        LOG.warning(f'Got timeout while trying to clone {repo_name}.')
        p.kill()

    shutil.rmtree(f'{repo_dir}/.git', ignore_errors=True)
    return repo_dir


def process_repo(repo_dir):
    """parse markdown code snippets.

    Args:
        repo_dir (str): directory name.

    Returns:
        List<Dict>
    """
    snippets = []
    snippets_dir = os.path.join(repo_dir, "snippets")
    for idx, file in enumerate(os.listdir(snippets_dir), start=1):
        name, ext = os.path.splitext(file)
        if ext.lower() != ".md":
            continue

        snippet_file = os.path.join(snippets_dir, file)
        LOG.info("Processing %s", file)
        with open(snippet_file, "r") as f:
            md_content = f.read()
            html_content = marko.convert(md_content)
            soup = BeautifulSoup(html_content)
            code_blocks = soup.find_all(
                "code", attrs={"class": [
                    "language-py",
                    "language-js",
                    "language-jsx",
                    "language-php",
                    "language-go",
                    "language-csharp"
                ]})

            try:
                snippet_code, usage_code = code_blocks
            except (IndexError, ValueError):
                LOG.warning(f"OOPS: could not parse code block from snippet %s: %s", file, soup)
                continue

            snippets.append({
                "name": name,
                "id": idx,
                "tag": code_blocks[0].get('class')[0].strip("language-"),
                "code": snippet_code.text.strip(),
                "usage": usage_code.text.strip()
            })

    LOG.info(
        "Successfully collected %d snippets from %s",
        len(snippets), os.path.basename(repo_dir)
    )
    return snippets


def download_problem_set(language_name, output_dir=None, clone_timeout=150, delete=False):
    """Download and process snippets from a 30-seconds repo, i.e `https://github.com/30-seconds/30-seconds-of-python`.

    Args:
        language_name (str): language name.
        output_dir (str): optional, output directory.
        clone_timeout (int): optional, timeout in seconds. default is 150.
        delete (bool): optional, delete repository after processing. default is False.

    Returns:
        List
    """
    repo_url = f"https://github.com/30-seconds/30-seconds-of-{language_name}"
    repo_dir = download_repo(repo_url, clone_timeout=clone_timeout, output_dir=output_dir)
    repo_dir = os.path.abspath(repo_dir)

    if os.path.exists(repo_dir):
        LOG.info(f"Successfully cloned repo {repo_url.rsplit('/')[-1]} into {repo_dir}")

        try:
            return process_repo(repo_dir)
        finally:
            if delete:
                shutil.rmtree(repo_dir, ignore_errors=True)

    else:
        LOG.error(f"failed to clone repo {repo_url.rsplit('/')[-1]} into {repo_dir}")


def get_prompt_from_code(code_str):
    """Split ``code_str`` to a <prompt, completion> based on indents.

    Args:
        code_str (str): code str.

    Returns:
        <before, after>
    """
    splits = list(
        split_before(
            code_str.splitlines(),
            lambda x: x and x[0].isspace(), maxsplit=1
        )
    )

    try:
        before_indent, after_indent = splits
        before_indent = "\n".join(before_indent)
        after_indent = "\n".join(after_indent)
    except (ValueError, IndexError):
        before_indent, after_indent = None, None

    return before_indent, after_indent


def get_test_from_usage(entry_point, code_str):
    """Extract a test function from a usage snippet.

    Args:
        code_str (str): code str.

    Returns:
        str
    """
    body_str = "def check(candidate):\n"
    prev = None
    for line in code_str.splitlines():
        actual, expected = None, None
        if line.startswith("#") and prev is not None:
            actual = prev.strip().replace(entry_point, "candidate")
            expected = line.strip("#").strip()
        elif "# " in line:
            parts = line.split("# ")
            if len(parts) == 2:
                actual, expected = parts
                actual = actual.strip().replace(entry_point, "candidate")
                expected = expected.strip()
            else:
                LOG.warning(code_str)
        if actual and expected:
            body_str += f"    assert {actual} == {expected}\n"
        else:
            body_str += f"    {line}\n"
        prev = line
    if body_str.count("\n") == 1:
        body_str += "pass"
    return body_str


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--language_name",
        type=str,
        default="python",
        choices=["python", "golang", "php", "react"],
        help="Language Name (i.e ``30-seconds-of-python``).",
    )

    parser.add_argument(
        '-v', '--verbose',
        help="Log Verbose",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()

    logging.basicConfig(
        level=args.loglevel,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M'
    )

    snippets = download_problem_set(args.language_name, delete=True)
    problems = []

    for snippet in tqdm.tqdm(snippets, total=len(snippets), desc="Snippets"):
        code_str = snippet["code"].strip()
        prompt, after_prompt = get_prompt_from_code(code_str)
        if not prompt:
            continue

        problem_dict = {
            "task_id": f"task/{snippet['id']}",
            "prompt": prompt,
            "canonical_solution": after_prompt,
            "entry_point": snippet["name"]
        }
        if args.language_name == "python":
            problem_dict["test"] = get_test_from_usage(snippet["name"], snippet["usage"])
        else:
            problem_dict["test"] = snippet["usage"]
        problems.append(problem_dict)

    problems_file = os.path.join(
        os.path.dirname(__file__), os.pardir, "data",
        f"30_seconds_of_{args.language_name}_problem.jsonl"
    )
    LOG.info("Writing %d problems to %s", len(problems), problems_file)
    srsly.write_jsonl(problems_file, problems)
