import argparse
import logging
import os
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
        "--diff",
        default=False,
        action="store_true",
        help="Output diff to file",
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

    if args.diff:
        args.diff_file = (
            args.sample_file
                .replace("data", "examples")
                .replace("samples", "problem")
                .replace(".jsonl", ".md")
        )
    else:
        args.diff_file = None

    return args


if __name__ == "__main__":
    args = parse_arguments()

    logging.basicConfig(
        level=args.loglevel,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M'
    )

    problems = {
        task["task_id"]: task
        for task in srsly.read_jsonl(args.problem_file)
    }

    if args.diff_file:
        os.makedirs(os.path.dirname(args.diff_file), exist_ok=True)
        out_file = open(args.diff_file, "w")
    else:
        out_file = sys.stdout

    for sample in tqdm.tqdm(srsly.read_jsonl(args.sample_file)):
        task_id = sample["task_id"]
        completion = sample["completion"]
        problem = problems[task_id]
        prompt = problem["prompt"]
        completion = sample["completion"].replace("\n\n", "\n    ")

        try:
            pos = completion.index("def ")
            completion = completion[:pos]
        except ValueError:
            pass

        completion = completion.rstrip()

        if completion:
            if out_file == sys.stdout:
                print(f"\033[1m{prompt}\033[0m{completion}", file=out_file)
                print(file=out_file)
            else:
                print(f"#### {problem['entry_point']} ({problem['task_id']})", file=out_file)
                print(file=out_file)

                print("```diff", file=out_file)
                for line in prompt.splitlines():
                    print(f"-{line}", file=out_file)
                for line in prompt.splitlines():
                    print(f"+{line}", file=out_file)
                for line in completion.splitlines():
                    print(f"+{line}", file=out_file)
                print("```\n", file=out_file)
