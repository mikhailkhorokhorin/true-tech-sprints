# Task 3. Submission

**Model:** Fable 5, default parameters, single pass with no manual edits.

## Prompt

```
# Task

Put together a personal audit: where AI saves my time. Rely only on the profile below, these are my real tasks, not hypotheticals.

# My profile

<workload>
Job: backend developer at Sber, the Manzherok project, a ski resort platform. I own the admin side: the infrastructure management API and the audit subsystem. 8-hour workday, 4–5 hours of it on code, the rest is calls and approvals.
Outside work: the Foodize startup, the Usability School online school, hackathons. Evenings and weekends, about 15 hours a week.
AI tool: Claude Code in the terminal only.
I do not do: code review for colleagues, onboarding newcomers.
Pet peeve: big-company bureaucracy.
</workload>

<stack>
Job: Python, FastAPI, Kafka, PostgreSQL (SQLAlchemy async, asyncpg), Pydantic, Docker. Architecture: domain / logic / infra / application / services.
Projects: same plus pgvector, Prometheus, Grafana, TypeScript.
</stack>

<what_i_do>
Job:
1. CRUD APIs in admin_backend: machinery, cameras, locations, zones, lifts; auto-generation of location keys. 5 times a week.
2. Audit subsystem: business and security events go through Kafka, shared_audit publishes, admin_audit consumes and stores them in the DB. 2 times a week.
3. Contracts between services: Pydantic schemas of Kafka messages in shared_backend, type discriminators, versioning. Rollout as a chain of MRs across repositories in strict order. 2 times a week.
4. PostgreSQL migrations: tables with backfill, audit tables, foreign keys, error codes. 2 times a week.
5. Environment: building dependencies for free-threaded Python 3.13, package conflicts. Once a week.
6. Writing up tasks and MRs: Jira descriptions, merge plans, tech docs. 4 times a week.

Outside work:
7. Foodize: a monorepo with backend, frontend, mobile, telegram-bot, miniapp; an AI agent with a pgvector-backed menu and streaming responses. 2 times a week.
8. Usability School: splitting a monorepo into 10 repositories, keeping shared and infra in sync. 2 times a week.
9. Hackathons: AIIJC, Alfa Future, True Tech. In waves several times a year.
</what_i_do>

# How to work

1. Take all nine profile items, one row per item. Keep the profile order: the six job items first, then Foodize, Usability School and hackathons.
2. Fill each table row using the columns from the "Answer format" section.
3. Convert all nine values of the "savings per week" column to minutes, add them up, and convert the sum back to hours and minutes. Put it in the "Total" line, the sum must match the column.

# How to estimate time

- "Time per run" is the duration of one execution, not a weekly total.
- Savings per run × frequency = savings per week. The arithmetic must add up.
- Estimates are conservative: a 20–40% gain on the task time, not 80%.
- Take the frequency from the profile as a whole number of times per week: weekly savings must come out as an exact number of minutes or hours, no "roughly" and no "~".
- Savings per row: no more than 1 hour a week. This rule outranks the 20–40% range: if a frequent task pushes past an hour, take a lower percentage instead of breaking the cap.
- Hackathons are an exception to the multiplication rule: in "how often" write "in waves several times a year", in "savings per run" put the time of one hackathon, and in weekly savings put 20–30 minutes as a year-round average. Do not multiply these two numbers.

# Content requirements

- Name specific modules from the profile: admin_backend, shared_audit, Kafka schemas, pgvector. "Code", "tests", "a service" will not do.
- "What stays with me" is my decision, my domain knowledge or my access to production data.
- Write in the first person, as my own audit.
- Scenarios must fit Claude Code in the terminal: editing files, generating code and tests, git, digging through logs.
- The row about writing up tasks must show that AI produces text drafts but does not change how fast approvals move.

# Answer format

A table with the columns:
Task | What I do | How often | Time per run | Where I apply AI | What AI does | What stays with me | Savings per run | Savings per week

"Where I apply AI" is the stage: requirements analysis, code draft, tests, debugging, description text. "What AI does" is the action at that stage.

Nine rows, one per profile item. Below the table, a "Total" line with the sum and one sentence on where the freed-up time goes.

The answer consists of two parts: one table and the "Total" line. Output only the final version: no intermediate versions, no recalculation traces, no verification reports, no disclaimers, no offers to redo. Nothing before, between or after.
```

## Model output

| Task | What I do | How often | Time per run | Where I apply AI | What AI does | What stays with me | Savings per run | Savings per week |
|---|---|---|---|---|---|---|---|---|
| CRUD APIs in admin_backend | I write endpoints for machinery, cameras, locations, zones, lifts and the auto-generation of location keys across the domain/logic/infra/application layers | 5 times a week | 100 min | Code draft | Lays a new entity out across the admin_backend layers: Pydantic schemas, router, SQLAlchemy model and pytest suite modeled on a neighboring entity | Rules for building location keys, links between zones and lifts, what to expose to the admin | 12 min | 1 hour |
| Audit subsystem | I route business and security events through Kafka: shared_audit publishes, the admin_audit consumer writes to the DB | 2 times a week | 120 min | Code draft | Writes the producer plumbing in shared_audit and the admin_audit consumer, key-based idempotency and serialization tests | Which actions count as security events and what must never go into the audit table | 30 min | 1 hour |
| Contracts between services | I edit Pydantic schemas of Kafka messages in shared_backend, type discriminators, versioning, and roll changes out as a chain of MRs | 2 times a week | 100 min | Requirements analysis | Checks the shared_backend schema against its usages in admin_backend, finds incompatible fields, suggests the MR order | The final call on the contract with neighboring teams and the timing of the production rollout | 30 min | 1 hour |
| PostgreSQL migrations | I write alembic migrations: audit tables, foreign keys, data backfill, error codes | 2 times a week | 90 min | Code draft | Generates upgrade/downgrade, a batched backfill script and verification SQL queries from the admin_backend SQLAlchemy models | Estimating data volume and locks on production, rollout order and access to production data | 25 min | 50 min |
| Environment | I build dependencies for free-threaded Python 3.13, untangle package conflicts, fix the Docker build | Once a week | 120 min | Debugging | Digs through the build log, finds the package with no free-threaded support, suggests versions and Dockerfile fixes | Deciding what to replace the incompatible package with and whether to stay on 3.13t at all | 35 min | 35 min |
| Writing up tasks and MRs | I write Jira descriptions, merge plans for MR chains, tech docs | 4 times a week | 40 min | Description text | Builds an MR description draft, a per-repository merge plan and a Jira task stub from the git diff and commit history | Sign-off with management and neighboring teams: the draft is ready sooner, but approval timelines do not move | 12 min | 48 min |
| Foodize | I grow the backend/frontend/mobile/telegram-bot/miniapp monorepo and an AI agent with a pgvector-backed menu and streaming responses | 2 times a week | 150 min | Code draft | Writes menu indexing in pgvector, the cosine-similarity query and SSE response streaming, plus fixes in telegram-bot and miniapp | The agent's output quality on real orders, menu structure and product decisions | 30 min | 1 hour |
| Usability School | I split the monorepo into 10 repositories and keep shared and infra in sync | 2 times a week | 120 min | Debugging | Carries history over with git filter-repo, fixes imports after extracting shared, patches CI and docker-compose in infra | Where to draw the repository boundaries and who gets access to the infrastructure | 30 min | 1 hour |
| Hackathons | I compete in AIIJC, Alfa Future, True Tech | In waves several times a year | 20 hours | Code draft | Quickly stands up a FastAPI service skeleton, writes the baseline and experiment plumbing, digs through logs of failed runs | Choosing the approach to the problem and what to show the judges | 5 hours | 25 min |

Total: 7 hours 38 minutes a week. The freed-up time goes to Foodize and hackathons, the things that move only on my decisions, not on my typing speed.

## Notes

The main risk is plausible but invented numbers. The prompt sets not a topic to muse on but a profile of nine real tasks with frequencies, and demands a row for each: no picking and choosing, and with that no temptation to invent a pretty example.

The calculation rules are strict: "savings per run × frequency = savings per week", a 20–40% gain, a one-hour cap per row. The cap is declared to outrank the range, otherwise the rules conflict on daily tasks and the model silently breaks one of them. Hackathons are carved out of the multiplication rule: their frequency cannot be expressed in times per week.

Summation is split into steps "convert to minutes, add up, convert back": with a plain "add up the column" the model did the math in its head and in one run was off by 20 minutes. Here 60+60+60+50+35+48+60+60+25 = 458 min = 7 h 38 min.

The row about writing up tasks deliberately shows the limit of AI's usefulness: it speeds up drafts, not approvals.
