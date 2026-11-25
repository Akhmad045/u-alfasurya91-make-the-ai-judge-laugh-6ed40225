# Make the AI Judge Laugh — the office password joke

[![Make the AI Judge Laugh](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/Akhmad045/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/Akhmad045/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

My entry for the [make.fun "Make the AI Judge Laugh" bounty](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225): a one-line joke about office life. Everyone who has worked in an office knows the pain of forced password rotation — a new secret every 90 days that nobody can remember. The joke turns that pain into the punchline: the one date the narrator can never forget is the last time they cried at their desk, so that date becomes the password.

## The line

> IT makes me change my password every 90 days, so now it's just the date I last cried at my desk.

96 characters in a single breath: a true office observation, then a surprise last word, and nothing wasted in between.

## How to run it

```sh
python3 main.py               # writes the joke to /output/entry.txt
python3 main.py --self-test   # checks the joke against the gate
python3 main.py --out /tmp/entry.txt   # write somewhere else instead
```

Everything the entry needs is `main.py`: it checks the line against the gate (1–200 characters, one line, no padding, plain UTF-8) and writes it byte-exact. No network access, no secrets, no third-party packages — plain Python 3.

Referral code: `4g7knchf`
