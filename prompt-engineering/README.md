# True Tech Sprint: Prompt Engineering with MWS AI

Write structured, reliable and applicable prompts with full context coverage. Evaluation criteria: context completeness, structure and clarity, quality and practical applicability of the result, reliability, appropriateness of the chosen approach.

## Tasks

| Task | What it is | Statement | Solution |
| --- | --- | --- | --- |
| 1 | Reply to a hostile client email in three tones, pick the best one | [TASK.md](task1/TASK.md) | [SUBMISSION.md](task1/SUBMISSION.md) |
| 2 | A glossary of five easily confused names for sprint newcomers | [TASK.md](task2/TASK.md) | [SUBMISSION.md](task2/SUBMISSION.md) |
| 3 | A personal audit of where AI saves my time, with checked arithmetic | [TASK.md](task3/TASK.md) | [SUBMISSION.md](task3/SUBMISSION.md) |
| 4 | Find the mistakes in an AI-generated answer, fix it, ship two reusable prompts | [TASK.md](task4/TASK.md) | [SUBMISSION.md](task4/SUBMISSION.md) |
| 5 | Compare three cloud plans and recommend one for an AI/ML platform, prose only | [TASK.md](task5/TASK.md) | [SUBMISSION.md](task5/SUBMISSION.md) |

## Evaluation criteria

**Solving speed.** The key priority.

**Context completeness.** The prompt must cover all essential requirements of the case: subtasks, input data, constraints, role, audience and the desired output format.

**Structure and clarity.** Instructions must be understandable and specific enough. The task is broken into steps, the output format is stated explicitly, without ambiguity.

**Quality and practical applicability of the result.** What gets evaluated is the model's final answer. The prompt must be phrased so that the model's output is substantive, coherent and ready to use without rework.

**Reliability.** The prompt must include safeguards against typical model failures. These may be instructions to verify facts, to rely only on the provided data, to flag uncertainty, format and tone constraints, and edge-case handling. The set of safeguards depends on the case: what is assessed is how well the author anticipated the risks specific to their own task.

**Appropriateness of the chosen approach.** The chosen instructions, examples and other techniques must be justified by the task and help produce a better result. What is assessed is not the number of techniques used but their practical value. The prompt must not contain redundant roles, repetitions, elaborate constructions or stages that do not improve the result. For example, adding chain-of-thought to a simple formatting task is a redundant technique, whereas few-shot examples for a task with a complex output format are justified.

## Scoring

Each criterion is scored from 0 to 2 points.

- **0 points.** The criterion is not met. A required element is missing, or the prompt does not produce a result that meets the requirements.
- **1 point.** The criterion is partially met. The main requirements are addressed, but there are noticeable gaps or inaccuracies, or the result needs substantial rework.
- **2 points.** The criterion is fully met. The requirements are addressed, the instructions are clearly formulated, and the resulting output fits the task and is practically applicable.
