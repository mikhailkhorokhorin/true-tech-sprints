# Task 1. Submission

**Model:** Fable 5, default parameters, single pass with no manual edits.

## Prompt

```
# The situation

I run the "AI scoring" project at an IT company. The client sent a sharp email and copied my manager. I have to answer today: draft three replies in different tones, pick one and explain why that one.

# The email we are answering

<incoming>
To: Prompt engineer. Cc: his manager
Subject: RE: "AI scoring" project status - URGENT

Good afternoon!

Let me say straight away that I am extremely unhappy with how this project is going. The pilot launch was agreed for July 3. Today is the 27th - no pilot, no information about a change of dates. At the steering committee you said "almost everything is ready". The marketing campaign is ready, we are losing money every day.

I ask you to provide the reasons for the delay, a realistic date, and a meeting with your manager. If I do not get an answer by the end of the week, I will escalate.
</incoming>

<for_my_eyes_only>
The delay is real: the security team requires an additional audit under Russian law.
Realistic pilot date: August 5.
At the steering committee I was talking about the code and did not budget time for approvals.
My manager knows about the situation.
</for_my_eyes_only>

# How to work

Do the first two steps silently, they do not go into the answer. The answer starts with the first letter.

Step 1. Work out what the client is asking for and what he wants beyond the facts. The sharp tone is a signal too: dates and reasons alone will not close this email. Keep that in mind while drafting.

Step 2. Collect the set of facts required in all three letters. Further down I call it "the six facts":
the delay, acknowledged without argument;
the reason, a mandatory review under Russian law;
a clarification about the steering committee: the estimate covered the code, approval time was not in it;
the date August 5;
agreement to a meeting with my manager present;
a note that the reply was sent inside the deadline he named.

Step 3. Write three letters. Their tone differs, but not through polite wording alone: each has its own opening and its own order of arguments.
the neutral one opens with status and runs through reason, date, next step;
the diplomatic one opens with regret over the missed date and leads to the meeting;
the confident one opens with the date and the plan, the reason comes later as an external circumstance.

Step 4. Match the letters against the situation. The client is counting losses, my manager is in copy, and the escalation is stated as a deadline rather than a vague threat. Pick the letter that removes the grounds for escalation without adding promises beyond the six facts.

# Boundaries

Each letter is 120 to 200 words of plain prose. The subject line and the signature "Best regards, [Name], project manager" do not count. No markup and no subheadings inside the letters.

Write your own subject line to match the letter, do not carry the "RE:" chain from the incoming email. All three subject lines differ.

Work only with the two blocks above. Do not introduce anything absent from them: compensations, discounts, interim dates, names, details of the audit procedure. Do not estimate the size of his losses or the cost of downtime on his behalf. Mention his losses only as his own words.

Acknowledge the delay as a circumstance. Do not admit team fault and do not call the reason a mistake.

Do not retell the "for my eyes only" block word for word. Speak about the steering committee as the area the estimate covered. Say no more about the security review than the fact that it is mandatory.

Give no promises beyond the six facts. Regular status updates, demos, promises to speed up the review and talk of changing the process are all off limits.

Do not answer sharpness with sharpness and do not argue about whether his emotions are justified. Officialese of the "in view of the aforementioned" kind is not needed either.

# Format

Option 1. Neutral
Subject: subject line
letter text

Option 2. Diplomatic
Subject: subject line
letter text

Option 3. Confident
Subject: subject line
letter text

Choice
I recommend: number and name.
Why: three to five sentences, each resting on a circumstance from step 4.
The other two: one sentence each on when they would fit.

The answer ends on that line. Do not add a self-check report, conclusions or remarks about your own work after it.

If an instruction can be read two ways, take the simple reading.
```

## Model output

**Option 1. Neutral**
Subject: "AI scoring" project status: reasons for the delay and the pilot date

Good afternoon. I am reporting the current project status. The pilot launch agreed for July 3 did indeed not happen, the delay is real and I will not dispute it. The reason is that before launch the product must pass a mandatory review for compliance with Russian law; without completing it the launch is impossible. Separately, on the steering committee: the "almost everything is ready" estimate referred to code readiness, approval time was not part of it, which is where the gap with your expectations on dates comes from. The realistic pilot launch date is August 5, named with the time to finish the mandatory review already included. You wrote that you are losing money every day, so I suggest we do not postpone the discussion: we are ready for a meeting with my manager present. Please propose a time that suits you and we will adjust on our side. I am sending this reply by the end of the week, inside the deadline you set in your email.

Best regards, [Name], project manager

**Option 2. Diplomatic**
Subject: "AI scoring" pilot: clarification on dates and a proposal to meet

Good afternoon. I am sorry that the launch agreed for July 3 did not happen on time and that you are only now receiving information about new dates: the delay is real and I am not going to dispute it. I understand that a marketing campaign is tied to the launch and that, in your words, you are losing money every day, so I am answering on the substance and within the deadline you set, by the end of the week. The reason for the delay is a mandatory review for compliance with Russian law, without which the launch is impossible. On the steering committee, let me explain: my estimate concerned code readiness, approval time was not part of it, which is why the picture sounded more optimistic than it turned out. The realistic pilot launch date is August 5. I consider your proposal to meet the right step and support it. We are ready to hold it, my manager will take part, he is aware of the situation. Please write which time suits you and we will fit your schedule.

Best regards, [Name], project manager

**Option 3. Confident**
Subject: "AI scoring" pilot: launch on August 5 and a project meeting

Good afternoon. The main point first: the realistic pilot launch date is August 5. I suggest planning around it, including the marketing campaign you mention. The nearest step is a meeting: we are ready for it, my manager will take part, and at the meeting we will go through the situation and the launch date. Now the reasons. I confirm the delay against the agreed July 3. The launch is held by an external circumstance, a mandatory review for compliance with Russian law that must be passed before the pilot. The August 5 date accounts for that review, which is what makes it realistic. On the steering committee: my estimate referred to code readiness, approval time was not part of it, hence the difference between what was said and the actual launch date. You set a reply deadline of end of week; this letter is sent within it. I am waiting for your options on meeting times and will adjust on our side.

Best regards, [Name], project manager

**Choice**

I recommend: Option 3. Confident.

Why: The client is counting losses every day, and a letter opening with the August 5 date immediately gives him something to plan against instead of excuses. My manager is in copy, so the text has to read as a managed situation with a plan rather than an admission of fault that can be quoted during escalation. The escalation is stated as a specific deadline of end of week, and this letter explicitly records that all three requirements, reasons, date and meeting, are closed inside that deadline, which removes the formal grounds for it. At the same time the confident option adds nothing beyond the six facts: the sense of control comes from the order of arguments, not from new promises.

The other two: the neutral one would fit if the correspondence were calm, with no stated escalation and no manager in copy; the diplomatic one if the main risk were damaged personal relations with the client rather than the escalation deadline and the cost of downtime.

## Notes

The prompt is built around six facts fixed before any letter is written. That way the tones differ in delivery rather than in the set of facts, and none of the client's three requirements drops out.

The first two steps are marked as internal. Without that the model printed its analysis of the requirements before the letters in some runs, and the output format drifted.

The internal context sits in its own tag under two bans: do not retell it verbatim and do not add your own judgements. Without the second one the model wrote about the cost of downtime, which is nowhere in the input. The client's losses may only be quoted as his own words.

The opening and the order of arguments are specified per letter. Without that the three options differed only in polite wording while sharing one structure. The selection criterion is stated explicitly as well, otherwise the choice drifted between runs.
