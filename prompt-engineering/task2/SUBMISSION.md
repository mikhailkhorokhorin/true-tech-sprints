# Task 2. Submission

**Model:** Fable 5, default parameters, single pass with no manual edits.

## Prompt

```
# Why this is needed

I am putting together a cheat sheet for people who have landed on True Tech Sprint for the first time. The names here look alike and sit one inside the other, so newcomers lose track of them. The cheat sheet has to sort out five names so that after reading it a person no longer mixes them up.

The reader is a competition participant. They do not know the structure of MTS, and they do not need it in any depth: it is enough to understand where they have ended up and who wrote the tasks they are solving.

# Facts

Everything you may use is collected below.

<nesting>
MTS includes MWS, MWS includes MWS AI. These are companies and divisions.
True Tech includes True Tech Champ and True Tech Sprint. This is a brand and the events inside it.
True Tech belongs to MTS. The tasks of the prompt engineering track are made by MWS AI.
</nesting>

<facts>
MTS, in full Mobile TeleSystems: a telecom operator, the parent company of the group.
MWS, in full MTS Web Services: the IT division of MTS, cloud and digital services.
MWS AI: the artificial intelligence line of work inside MWS, the author of the prompt engineering track tasks.
True Tech: the IT brand of MTS, it covers conferences, championships and sprints.
True Tech Champ: the championship of the True Tech brand. There are two tracks. "Algorithmic" is individual, olympiad style problems, prize pool 2,750,000 RUB. "Robot programming" is teams of two to four people, robot dogs and ROS2, prize pool 7,500,000 RUB. The final of both tracks is on 22 October 2026 in Moscow.
True Tech Sprint: a series of short online competitions of the same brand. Prompt engineering 27.07–02.08, development 10.08–16.08, DevOps 24.08–30.08. The prize pool of the prompt engineering track is 200,000 RUB.
</facts>

# What to do

We are sorting out five names: MTS, MWS, MWS AI, True Tech and True Tech Champ. True Tech Sprint does not get a row of its own, it is the competition the reader is already at. But it is present in the facts, and it is needed in the field about confusion: it is the one most often mixed up with Champ.

Step 1. Before writing, decide for each name which type it belongs to: a company, a division inside a company, a line of work inside a division, a brand or an event of a brand. The type will be needed in the first field. The difference between a division and a line of work here is simple: the division is MWS as a whole, the line of work is a part inside it.

Step 2. Fill in three fields for each name. In the table they are called "What it is", "Where you meet it" and "What it gets confused with".

What it is: one or two sentences, always with the type from step 1 and with an indication of what the name sits inside.

Where you meet it: how this name touches a sprint participant. For MWS AI and True Tech there is a direct situation here, the participant sees them with their own eyes. For MTS, MWS and Champ there is no direct situation, and there is no need to invent one, explain the link instead: through whom they relate to the sprint and why the participant hears about them at all. The wording "no data" does not work in this field, the link follows from the nesting block.

What it gets confused with: one sentence about the difference from the paired name. The pairs are these. MTS gets confused with True Tech, True Tech with MTS, MWS with MWS AI, MWS AI with MWS, True Tech Champ with True Tech Sprint. Two pairs are mirrored, and that is not a typo: the wordings in them have to look from different sides rather than repeat each other. For MTS explain that a company is not a brand, for True Tech the other way round, that a brand is not a separate firm. Separate MWS and MWS AI the same way. Dates, sums and track listings do not go into this field.

Step 3. After the table, draw the nesting scheme in words, three to five lines.

# Text requirements

The tone is that of work correspondence with a colleague: short phrases, ordinary words.

Do not write "comprehensive solutions", "synergy", "ecosystem", "digital transformation", "as part of the implementation". This kind of language is exactly why cheat sheets go unread.

Spell out MTS and MWS in full on first mention, the expansions are in the facts. The other names have no expansions, and there is no need to invent them.

Each field reads separately from its neighbours and makes sense on its own.

In each of the first two fields no more than two sentences, counted per field separately. The only exception is the definition of True Tech Champ, it may have three, there are two tracks there. In the other definitions take from the facts only what tells the name apart from its neighbour, do not copy them out in full.

Numbers from the facts block may be used. Inventing new numbers, dates, names and product names is not allowed. If there is not enough data for a field, write exactly that: "no data".

# Format

A table of four columns: Name | What it is | Where you meet it | What it gets confused with

Five rows, in this order: MTS, MWS, MWS AI, True Tech, True Tech Champ.

Under the table a heading "How it all nests" and the scheme.

The answer ends with the scheme. Do not add check reports, conclusions or comments after it.
```

## Model output

| Name | What it is | Where you meet it | What it gets confused with |
|---|---|---|---|
| MTS | The company Mobile TeleSystems: a telecom operator, the parent company of the group. Everything else in this cheat sheet belongs to it. | It does not show up at the sprint directly: the sprint runs under the True Tech brand, and that brand belongs to MTS, which is why the name comes up. | With True Tech: MTS is a company, while True Tech is only its sign board for IT events, not a separate organisation. |
| MWS | The division MTS Web Services inside the company MTS: the IT division, cloud and digital services. | A participant does not see it directly: MWS AI works inside MWS and makes the prompt engineering track tasks, hence the name being around. | With MWS AI: MWS is the whole division, not just its AI part. |
| MWS AI | The artificial intelligence line of work inside the MWS division. The author of the prompt engineering track tasks. | A direct situation: the tasks a participant solves on the prompt engineering track were written right here. | With MWS: MWS AI is only one line of work inside MWS, not the entire division. |
| True Tech | The IT brand of the company MTS. It covers conferences, championships and sprints. | A direct situation: the competition the participant is at right now runs under this brand. | With MTS: True Tech is not a separate firm but a brand under which the company MTS runs its IT events. |
| True Tech Champ | A championship, an event of the True Tech brand. There are two tracks: "Algorithmic", individual, olympiad style problems, prize pool 2,750,000 RUB; "Robot programming", teams of two to four people, robot dogs and ROS2, prize pool 7,500,000 RUB. The final of both tracks is on 22 October 2026 in Moscow. | You will not meet it at the sprint: it is a neighbouring event of the same True Tech brand, so the name flashes by next to your competition. | With True Tech Sprint: Champ is a separate big championship, while Sprint is a series of short online competitions, and the participant is at Sprint right now. |

How it all nests

MTS is a company, everything below belongs to it.
Inside MTS there is the MWS division, and inside MWS the MWS AI line of work.
MTS has an IT brand, True Tech.
Inside True Tech there are events: True Tech Champ and True Tech Sprint.
You are at True Tech Sprint, and the prompt engineering track tasks are made by MWS AI.

## Notes

The statement contains not a single fact, only five names. Hence the main risk: the model reaches into its memory and invents expansions, sums and dates. So I put the verified facts straight into the prompt, and in two separate blocks. Nesting sits apart from the definitions, because a newcomer's confusion rests exactly on the nesting.

In the Q&A the organisers said the goal is to get the terms right, and that if the model lacks context, you should find a way to fix that. Facts in the prompt are that way: the task moves from "recall it" mode into "state it from the data" mode.

The step where the type of each name is decided comes before the table is filled in. Without it the definitions came out so that you could not tell whether the thing was a company, a brand or an event, and the whole confusion stands on precisely that distinction.

The pairs in the confusion column are given as a list, including the two mirrored ones. The model used to write the same thing twice in them, so I said directly that the wordings must look from different sides: for MTS explain that a company is not a brand, for True Tech the other way round. You can see that in the answer.

True Tech Sprint was left out of the table on purpose, it is the competition the reader is already sitting at. But it is in the facts and it is needed in the pair for Champ, so its status had to be spelled out separately, otherwise the model kept adding a sixth row.
