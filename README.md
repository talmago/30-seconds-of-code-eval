# 30-seconds-of-code-eval

An evaluation harness for [30-seconds-of-code](https://www.30secondsofcode.org/) snippets, in similar to HumanEval
problem solving dataset described in the
paper "[Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)".

In contrast to `HumanEval`, a dataset of 164 hand-written python programming problems, we
use [30-seconds-of-code](https://www.30secondsofcode.org/)
to build few short code snippets datasets, similar in structure to HumanEval,
in [Python](https://github.com/talmago/30-seconds-of-code-eval/blob/master/examples/30_seconds_of_python.md)
, [React](https://github.com/talmago/30-seconds-of-code-eval/blob/master/examples/30_seconds_of_react.md)
, [Go](https://github.com/talmago/30-seconds-of-code-eval/blob/master/examples/30_seconds_of_golang.md)
and [PHP](https://github.com/talmago/30-seconds-of-code-eval/blob/master/examples/30_seconds_of_php.md).

## Quick Setup

Clone project

```sh
$ git clone git@github.com:talmago/30-seconds-of-code-eval.git
```

Install dependencies

```sh
$ pip install -r requirements.txt
```

> *Notice*: python 3.7 or later is a requirement.
> If you use conda, follow these [instructions](https://github.com/openai/human-eval#installation).

## Usage

##### Build a problem set

```sh
$ python 01_download_problem_set.py --language_name python
```

Output will be saved
to [data/30_seconds_of_python_problem.jsonl](https://github.com/talmago/30-seconds-of-code-eval/blob/master/data/30_seconds_of_python_problem.jsonl)
.

#### Collect samples (via [Codex](https://openai.com/blog/openai-codex/))

```sh
$ OPENAI_API_KEY=XXXX python 02_get_completions_from_codex.py data/30_seconds_of_python_problem.jsonl \
  --model_name davinci-codex \
  --max_length 70 \
  --temperature 0.8
```

Output will be saved
to [data/30_seconds_of_python_samples.jsonl](https://github.com/talmago/30-seconds-of-code-eval/blob/master/data/30_seconds_of_python_samples.jsonl)
.

#### Preview

```sh
$ python 03_print_code_examples.py data/30_seconds_of_python_samples.jsonl --diff
```

Output will be saved
to [examples/30_seconds_of_python.md](https://github.com/talmago/30-seconds-of-code-eval/blob/master/examples/30_seconds_of_python.md)

#### Evaluation

Coming soon ...

## References

[1] [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)

```
@article{chen2021codex,
  title={Evaluating Large Language Models Trained on Code},
  author={Mark Chen and Jerry Tworek and Heewoo Jun and Qiming Yuan and Henrique Ponde de Oliveira Pinto and Jared Kaplan and Harri Edwards and Yuri Burda and Nicholas Joseph and Greg Brockman and Alex Ray and Raul Puri and Gretchen Krueger and Michael Petrov and Heidy Khlaaf and Girish Sastry and Pamela Mishkin and Brooke Chan and Scott Gray and Nick Ryder and Mikhail Pavlov and Alethea Power and Lukasz Kaiser and Mohammad Bavarian and Clemens Winter and Philippe Tillet and Felipe Petroski Such and Dave Cummings and Matthias Plappert and Fotios Chantzis and Elizabeth Barnes and Ariel Herbert-Voss and William Hebgen Guss and Alex Nichol and Alex Paino and Nikolas Tezak and Jie Tang and Igor Babuschkin and Suchir Balaji and Shantanu Jain and William Saunders and Christopher Hesse and Andrew N. Carr and Jan Leike and Josh Achiam and Vedant Misra and Evan Morikawa and Alec Radford and Matthew Knight and Miles Brundage and Mira Murati and Katie Mayer and Peter Welinder and Bob McGrew and Dario Amodei and Sam McCandlish and Ilya Sutskever and Wojciech Zaremba},
  year={2021},
  eprint={2107.03374},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```
