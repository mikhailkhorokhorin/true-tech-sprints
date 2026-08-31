# Task 5. Submission

**Model:** Fable 5, default parameters, single pass with no manual edits.

## Prompt

```
# What we are deciding

We are picking a cloud for an AI/ML platform: we train models and we run inference under load. The platform lives for years, so engineering time costs no less than the provider's invoice. The CTO reads this analysis before signing the contract, and he needs to understand not only who wins but what he pays for that win.

# Three offers

<first>
Up to 32 vCPU, 128 GB RAM. GPU A100. S3 from 1.5₽/GB/month. PostgreSQL, MySQL, ClickHouse, MongoDB. SLA 99.95%. Support: email around the clock, phone during working hours, dedicated account manager once spend reaches 500k/month. From 1.2₽/hour per vCPU. FZ-152, GOST.
</first>

<second>
Up to 64 vCPU, 512 GB RAM. GPU V100 and A100. S3 from 1.8₽/GB/month. PostgreSQL, MySQL, Tarantool, ClickHouse. SLA 99.99%. Support around the clock, response to critical within 15 minutes. From 1.0₽/hour per vCPU. FZ-152, PCI DSS. Managed Kubernetes, CDN.
</second>

<third>
Up to 48 vCPU, 256 GB RAM. GPU A100 and H100. S3 from 1.3₽/GB/month. PostgreSQL, ClickHouse. SLA 99.95%. Support around the clock, dedicated account manager once spend reaches 300k/month. From 1.1₽/hour per vCPU. FZ-152, ISO 27001.
</third>

# How to work through it

Step 1. Go through nine parameters: CPU and memory, GPU, S3 price, database lineup, SLA, support terms, vCPU price, certifications, managed services.

Step 2. For each parameter first put the values side by side, then name the strongest one with the numbers. If two are strongest, name both at once and do not reverse the decision inside the paragraph. If the parameters do not compare directly and the answer depends on what the company does, say so plainly and explain which option sits closer to an AI/ML platform.

Step 3. The specs do not answer three questions, and the decision depends on them. First: what is at risk of going wrong during rollout. Second: how mature the layer around raw compute is, meaning storage, analytics and getting a model into production. Third: what you can actually lean on the moment something breaks. Step 1 compares promises, here say what those promises are worth.

Step 4. Name the choice and its price: what is given up along with that decision.

# How to weigh a parameter

Assign the weights yourself. Here is what to lean on.

The parameters are not equal to each other. For each one ask what it actually constrains: training, inference, or engineers' working hours. The one carrying the main load weighs more than the one that just saves money.

Turn differences into something understandable. Count SLA as minutes of downtime per month, GPU generations as training speed. Hardware numbers can and should be quoted, that is exactly what domain knowledge is for.

For money take a single baseline and name it in the answer: 64 vCPU around the clock and 100 TB in S3. The first offer caps out at 32 vCPU, so for it compute the same load across two machines and say that it does not fit into a single instance. Prices are given as "from", so calculate at the lower bound and write "at least this much".

A missing managed service is not zero, it is work the team takes on. Count that as the price of the decision.

Separate what limits the model itself from what limits the surrounding layer: storage, analytics, getting into production.

# Boundaries

Do not attribute properties to the offers that are not in the blocks: regions, autoscaling, disk sizes, provider names, discounts. At the same time domain understanding is required, without it there is no comparison: how H100 differs from A100, what SLA means, what it costs to run a cluster yourself. The ban covers invented specs, not knowledge of the technology.

Whatever is not written in a block, treat as absent for the comparison. If managed Kubernetes is not listed in an offer, then it is not there, and the cluster work falls on the team.

Do not declare a winner by the number of parameters won. Weight counts, not the number of ticks.

In the choice, name the condition under which it switches to a different offer.

There is enough data for all nine parameters, refusing to compare is not allowed. Saying that for a given parameter the answer depends on the company profile is still allowed: that is also a conclusion from the data.

# Format

Connected text in paragraphs, no tables in any form: not as markup, not as rows of vertical bars, not as columns made of spaces. Do not list the parameters as a list, each one goes inside a sentence together with its leader and its numbers.

Order: comparison by parameters, then the three answers from step 3, then the choice with its condition.

No headings inside the answer. Group the nine parameters by meaning so the whole thing fits into eight to twelve paragraphs: count money in one place, handle related parameters together. End with the choice, no summaries about your own work and no offers to improve anything.

If an instruction can be read two ways, take the simple reading.
```

## Model output

On CPU and memory the positions are these: the first offer gives up to 32 vCPU and 128 GB RAM, the second up to 64 vCPU and 512 GB, the third up to 48 vCPU and 256 GB, and the strongest here is the second, because only it fits our baseline load into a single instance, while 512 GB of memory leaves headroom for data preparation and large batches, where it is convenient to hold the dataset in memory whole. The first offer, capped at 32 vCPU, forces the same load to be cut across at least two machines, and that is already a distributed configuration with its own network connectivity and its own failure modes.

On GPU the first offer gives A100, the second V100 and A100, the third A100 and H100, and the strongest is the third. On training transformer models the H100 is roughly two to three times faster than the A100 thanks to higher bandwidth memory and FP8 support: training that takes a week on A100 fits into two or three days on H100, and that converts directly into the number of experiments the team gets through. The V100 in the second offer is a generation behind the A100, roughly half the training speed, and is better suited to inference on small models than to serious training.

I count money on a single baseline, and I name it: 64 vCPU around the clock (730 hours a month, that is 46,720 vCPU-hours) and 100 TB in S3, prices taken at the lower bound of "from", so every figure is "at least this much". On vCPU the leader is the second offer: 1.0₽/hour against 1.1 for the third and 1.2 for the first, which gives at least 46,720₽ a month against 51,392₽ and 56,064₽, and for the first offer those 56 thousand are spread across two machines, because 64 vCPU does not fit into a single instance. On S3 the leader is the third: 1.3₽/GB/month against 1.5 for the first and 1.8 for the second, which on 100 TB is at least 130,000₽ against 150,000 and 180,000. The totals on the baseline: the third at least 181,392₽/month, the first at least 206,064₽, the second at least 226,720₽, and the cheapest vCPU does not save the second, because at AI/ML platform volumes storage drives the bill, and a difference of 0.5₽/GB between the second and the third is 50 thousand a month for every 100 TB, and there will be more data over time, not less.

On databases the first offer gives PostgreSQL, MySQL, ClickHouse and MongoDB, the second PostgreSQL, MySQL, Tarantool and ClickHouse, the third only PostgreSQL and ClickHouse. On breadth there are two strongest, the first and the second, four managed database engines each, and past that the answer depends on the company profile: for document data MongoDB in the first is worth more, for fast feature serving into inference Tarantool in the second sits closer. For an AI/ML platform the base pair is PostgreSQL for metadata and ClickHouse for inference log analytics, and all three have it, so the third does not drop out here, but everything beyond that pair its team stands up itself.

On SLA the second offer promises 99.99%, the first and third 99.95%, and the leader is the second by a noticeable margin once the percentages are converted into minutes: 99.95% is up to 22 minutes of unavailability per month, 99.99% up to 4.4 minutes. For inference under load, where an outage is visible to users immediately, a fivefold difference in allowed downtime is not cosmetic, these are different classes of promise.

On support the leader is also the second, the only one with a measurable commitment: around the clock and a response to critical within 15 minutes. The third gives a round-the-clock line with no stated response time and an account manager from 300 thousand of monthly spend, the first is the weakest: phone only during working hours, email at night, manager from 500 thousand. On the managers specifically: on the baseline the bill for the third is around 181 thousand, for the first around 206, meaning neither reaches the 300 and 500 thousand thresholds, and the manager stays a promise for later rather than a property of the contract.

On certifications FZ-152 is present in all three, and it is the mandatory floor for personal data in Russia, so the parameter comes down to the extras: GOST in the first matters if the platform targets the public sector, PCI DSS in the second if payment data passes through it, ISO 27001 in the third is the general information security management standard that corporate customers most often ask about during presales. Here the answer honestly depends on the company profile; for a typical AI/ML platform with no payments and no government contracts, ISO 27001 sits closest, meaning the third.

On managed services the strongest is the second, and here it is the only one: managed Kubernetes and CDN, while the first and third list no managed services in their blocks, so for the comparison they do not have any. This is not a zero difference but work the team takes on: a self-run Kubernetes cluster for inference means installation, upgrades, security, on-call rotations and a constant visible share of engineering time, effectively part of an SRE headcount across the whole life of the platform, and since the platform lives for years, that price multiplies by years.

Now the three questions the specs do not answer, starting with rollout risk. In the first offer the risk is built into the ceiling: 32 vCPU means the platform lives on a distributed configuration from day one, and everything from training to serving gets more complicated for no gain. In the third the risk is that between "we got H100" and "the model answers users" lies the entire production serving infrastructure, which will have to be built by hand, and the launch date depends not on the provider but on your own team. In the second the risk is smaller and of a different kind: training on A100 is slower than it could be on H100, and if the research cycle becomes the bottleneck, it will show up not as an outage but chronically, as fewer experiments per unit of time.

The second question is the maturity of the layer around compute, and here the picture is sharper than in step 1. The second offer is the only one where a platform is visible rather than a pile of hardware: managed Kubernetes covers getting a model into production, CDN covers serving under load, ClickHouse covers analytics, Tarantool covers fast data delivery into inference. The first and third are essentially compute nodes with disks and a couple of database engines: the strong core in the third with H100 and the broad database lineup in the first do not change the fact that serving, orchestration and everything around the model are assembled by the team itself, and the promises of those offers are worth exactly what the engineering time to build the missing pieces costs.

The third question is what to lean on the moment something breaks. An SLA is a promise of compensation, not a promise of a fix: the 99.99% of the second offer will not bring failed inference back up on its own. What you can actually lean on is whatever is verifiable at three in the morning, and here the second has the only measurable thing across all three blocks, a response to critical within 15 minutes. In the third, round-the-clock support with no response deadline means "someone will get back to us eventually", in the first at night formally only email remains, which means at the worst possible moment the platform is effectively on its own. In an incident, the promises from step 1 are worth this much: the second has a procedure, the third has an on-call with no obligations, the first has an answering machine.

I choose the second offer. For a platform that lives for years and runs inference under load, the decision is made not by peak specs but by the operational layer: managed Kubernetes instead of your own cluster, 4.4 minutes of allowed downtime instead of 22, and 15 minutes to a response on critical, and that is what saves the most expensive thing, engineering time, which is why this analysis was run in the first place. The price of that choice is concrete: training stays on A100 and runs two to three times slower than it could on H100 in the third, the bill on the baseline is at least 226,720₽ a month against 181,392₽ for the third, and the gap will grow along with the data volume because of the most expensive S3, 1.8₽/GB against 1.3. The choice switches to the third offer if the platform's center of gravity moves from inference to training: when the queue of GPU experiments becomes the bottleneck before production stability does, the two to threefold speedup of H100 and the cheapest storage outweigh managed Kubernetes, provided the team is ready to take the cluster and the serving layer on itself.

## Notes

The statement contradicts itself: "bring them together into a single table" and "send the answer as text, not as a table". I split that across levels. Reducing them to shared parameters is a comparison operation, text is a requirement on the output. The table stays in the reasoning, prose goes out, and the ban is written into the prompt together with the workarounds: rows of vertical bars, columns made of spaces, enumeration as a list.

The second trap is that the data pushes toward the wrong choice. The second offer takes six parameters out of nine, so the prompt explicitly forbids declaring a winner by tick count, and instead sets a principle: for each parameter, ask what it constrains, training, inference, or engineers' working hours.

Ready-made conclusions are deliberately absent from the prompt. In an early version I hinted that 99.95 against 99.99 is 22 and 4 minutes, and the model simply rewrote the hint. I replaced it with the principle "turn differences into something understandable", and it did the arithmetic itself and more precisely: 730 hours in a month, 46,720 vCPU-hours, the total bill on a single baseline. From the same source came a conclusion I never planted: the bill does not reach the 300 and 500 thousand account manager thresholds, so the manager is a promise for later.

The single baseline had to be not only set but also repaired: the first offer caps at 32 vCPU, and it physically does not fit into a 64 vCPU baseline. Until that was spelled out, the model either quietly counted at 32 or got confused. Now the prompt says to compute the same load across two machines and to state that limit out loud.
