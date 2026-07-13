# Canonical Prompts

Canonical owner: this file.

Do not duplicate these prompts in other modules. Reference this file instead.

## Prompt Metadata Standard

Each prompt includes purpose, user, inputs, output format, constraints, uncertainty handling, human judgment points, failure conditions, version, and owner.

## Diagnostic Prompt v0.2

Purpose: diagnose operational friction by mapping symptoms to knowledge carriers, judgment dependencies, workflow fragility, and small interventions.

User: diagnostic agent or human operator.

Required inputs:

- organization description;
- observed symptoms;
- examples or artifacts;
- people involved;
- tools involved;
- known constraints.

Prompt:

```text
Analyze the supplied organization context using the Operational Knowledge Method.

Separate observations from inferences.

Identify:
1. observable operational symptoms;
2. evidence for each symptom;
3. where relevant knowledge or judgment currently resides;
4. whether the issue reflects concentration, fragmentation, tacit judgment, repeated correction, manual translation, tool mismatch, AI instability, or missing ownership;
5. risks if unchanged;
6. the smallest useful intervention using existing people and tools first;
7. missing information;
8. confidence level;
9. human judgment required.

Do not recommend new software unless the evidence shows existing people and tools cannot address the first useful intervention.

Return:
- executive summary;
- findings table;
- prioritized first intervention;
- questions to ask next;
- confidence and evidence limits.
```

Failure conditions: no evidence supplied, request for guaranteed results, or request to bypass human judgment.

## Qualification Prompt v0.2

Purpose: decide whether the organization is a fit for Operations Support.

Required inputs: diagnostic findings, conversation record, access, authority, timing, budget signal, implementation capacity.

Prompt:

```text
Evaluate fit for a small Operations Support engagement.

Classify the opportunity as:
- good fit;
- possible fit with questions;
- not now;
- refer elsewhere;
- no action.

Use these criteria:
- real recurring operational friction;
- evidence access;
- authority to act;
- willingness to make small changes;
- fit with existing people/tools-first approach;
- commercial viability;
- trust and timing.

Identify disqualifiers, uncertainty, human judgment required, and the next best action.

Do not approve pricing, scope, or commitments. Prepare the decision package for Damian.
```

## Translation Prompt v0.2

Purpose: convert internal analysis into client-recognizable language.

Prompt:

```text
Translate the internal finding into plain client language.

Rules:
- lead with what the client experiences;
- avoid AI, governance, and architecture language unless the client used it first;
- preserve uncertainty;
- do not exaggerate evidence;
- one idea per sentence;
- include the smallest practical next step.

Return:
1. short finding;
2. why it matters;
3. likely cause;
4. evidence;
5. what we do not know;
6. recommended next step.
```

## Implementation Planning Prompt v0.2

Purpose: design one small improvement.

Prompt:

```text
Create an implementation plan for the approved intervention.

Prefer existing people and tools.

Return:
- problem being addressed;
- intervention;
- owner;
- users;
- steps;
- asset to create or update;
- training or handoff;
- measurement;
- risks;
- rollback;
- review date.

Do not expand scope beyond the approved intervention.
```

## Learning Extraction Prompt v0.2

Purpose: convert outcomes and corrections into repository learning.

Prompt:

```text
Extract learning from this engagement or decision.

Separate:
- observation;
- inference;
- hypothesis;
- recommendation;
- human correction;
- action;
- outcome;
- reusable pattern;
- evidence level;
- repository update required.

Do not promote a pattern into methodology unless evidence level and human approval support it.
```
