import argparse
import difflib
import logging
import os
import re
import sys
import srsly
import tqdm


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "sample_file",
        type=str,
        help="Sample file",
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

    args.problem_file = args.sample_file.replace("samples", "problem")

    if not os.path.exists(args.problem_file):
        raise IOError(f"problem set does not exist at {args.problem_file}")

    args.diff_file = (
        args.sample_file
            .replace("data", "examples")
            .replace("samples", "problem")
            .replace(".jsonl", ".md")
            .replace("_problem", "")
    )

    args.language_name = re.search(
        "30_seconds_of_(.+)_samples.jsonl", args.sample_file).group(1)

    if args.language_name == "react":
        args.language_name = "javascript"

    return args


if __name__ == "__main__":
    args = parse_arguments()

    logging.basicConfig(
        level=args.loglevel,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M'
    )

    samples = {}
    for sample in srsly.read_jsonl(args.sample_file):
        samples.setdefault(sample["task_id"], []).append(sample)

    problems = {
        task["task_id"]: task
        for task in srsly.read_jsonl(args.problem_file)
    }

    os.makedirs(os.path.dirname(args.diff_file), exist_ok=True)
    out_file = open(args.diff_file, "w")

    for task_id, problem in tqdm.tqdm(problems.items()):
        prompt = problem["prompt"]
        canonical = problem["canonical_solution"]

        print(f"### {problem['entry_point']} ({problem['task_id']})", file=out_file)
        print(file=out_file)

        print("#### canonical solution", file=out_file)
        print(file=out_file)
        print(f"```{args.language_name}", file=out_file)
        print(f"{prompt}\n{canonical}", file=out_file)
        print("```", file=out_file)
        print(file=out_file)

        for idx, sample in enumerate(samples[task_id]):
            completion = sample.get("completion")

            if completion.startswith("\n") and not canonical.startswith("\n"):
                canonical_solution = f"{prompt}\n{canonical}"
            else:
                canonical_solution = f"{prompt}{canonical}"
            canonical_solution = canonical_solution.splitlines()
            solution = (prompt + completion).splitlines()[:len(canonical_solution) + 5]

            if args.language_name == "react":
                ext = ".jsx"
            elif args.language_name == "golang":
                ext = ".go"
            elif args.language_name == "php":
                ext = ".php"
            else:
                ext = "py"

            diff_gen = difflib.unified_diff(
                canonical_solution, solution,
                fromfile=f"canonical.{ext}",
                tofile=f"solution{idx}.{ext}"
            )

            print(f"#### solution {idx}", file=out_file)
            print(file=out_file)
            print("```diff", file=out_file)
            for diff_line in diff_gen:
                print(diff_line, file=out_file)
            print("```\n", file=out_file)
