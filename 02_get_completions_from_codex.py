import argparse
import logging
import os
import srsly
import requests
import tqdm

LOG = logging.getLogger(__name__)


def generate(
        prompt,
        max_tokens=50,
        num_results=5,
        temperature=0.8,
        top_p=0.9,
        model_name="davinci-codex",
        line=False
):
    """Generate a snippet with Codex."""
    token = os.getenv("OPENAI_API_KEY")
    assert token, "OPENAI_API_KEY is set in your env ?!"

    url = f"https://api.openai.com/v1/engines/{model_name}/completions"
    headers = {"Authorization": f"Bearer {token}"}
    json_payload = {
        "prompt": prompt,
        "n": num_results,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p
    }
    if line:
        json_payload["stop"] = "\n"

    try:
        r = requests.post(url, headers=headers, json=json_payload)
    except requests.exceptions.ConnectionError:
        LOG.error("OOPS: codex connection error")
        return

    r.raise_for_status()
    return r.json()


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "problem_file",
        type=str,
        help="Problem set",
    )

    parser.add_argument(
        "--model_name",
        type=str,
        default="davinci-codex",
        help="Codex model",
    )

    parser.add_argument(
        "--max_length",
        type=int,
        default=50,
        help="Max length",
    )

    parser.add_argument(
        "--temperature",
        type=float,
        default=0.8,
        help="temperature",
    )

    parser.add_argument(
        "--top_p",
        type=float,
        default=0.9,
        help="top_p",
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

    samples = []
    problems = list(srsly.read_jsonl(args.problem_file))

    try:
        for problem_dict in tqdm.tqdm(problems, total=len(problems), desc="problems"):
            if "prompt" not in problem_dict:
                LOG.warning("No prompt found in %s", problem_dict)
                continue

            resp = generate(
                problem_dict["prompt"],
                max_tokens=args.max_length,
                temperature=args.temperature,
                top_p=args.top_p,
                model_name=args.model_name
            )

            if not resp:
                LOG.warning("No response for prompt: %s", problem_dict["prompt"])
                continue

            for choice in resp["choices"]:
                samples.append({
                    "task_id": problem_dict["task_id"],
                    "completion": choice["text"]
                })
    finally:
        if samples:
            out_file = args.problem_file.replace("problem", "samples")
            LOG.info("Writing %d samples to %s", len(samples), out_file)
            srsly.write_jsonl(out_file, samples)
