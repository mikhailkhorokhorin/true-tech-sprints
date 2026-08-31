# True Tech Sprint: Development with MWS DevTools

Three algorithmic problems solved in Python. The sprint is judged on solving speed, correctness against hidden tests, and mandatory use of the MWS DevTools plugin (built on the MWS GPT Model Hub).

## Tasks

| Task | What it is | Statement | Solution |
| --- | --- | --- | --- |
| 1 | Count prime phone numbers with a given prefix, plus the VIP subset | [TASK.md](task1/TASK.md) | [submission.py](task1/submission.py) |
| 2 | Probability that a random string is an MTS-string, modulo 998244353 | [TASK.md](task2/TASK.md) | [submission.py](task2/submission.py) |
| 3 | Count k-stable MTS-strings of length n, modulo 998244353 | [TASK.md](task3/TASK.md) | [submission.py](task3/submission.py) |

Each `submission.py` is the exact code accepted by the platform.

## Evaluation criteria

**Solving speed.** The key priority — the leaderboard ranks by total time across the three tasks; the top places submit all three within roughly two minutes.

**Correctness.** A task counts only if every hidden test passes. Each task has 21 tests worth 100 points.

**Mandatory use of MWS tools.** Judged by the number of requests and the total number of tokens spent on the registered email, not by prompt contents. Only the top of the leaderboard is checked by hand.

## Timing model

The timer for a task starts when it is opened and stops when the run is submitted. Tasks are opened one at a time, solved from a prepared answer, and closed immediately — a run is mandatory, and re-runs add time. Plugin token traffic is not tied to time and can be generated after submission.
