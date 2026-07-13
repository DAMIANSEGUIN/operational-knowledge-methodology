# Operational Knowledge Method

## Canonical Status

- Status: approved controlled methodology v0.2.0
- Owner: `03_methodology/OPERATIONAL_KNOWLEDGE_METHOD.md`
- Source basis: `PROJECT.md`, `01_strategic_review/STRATEGIC_REVIEW.md`, `02_gap_analysis/GAP_ANALYSIS_v1.md`, and the Operations Support Field Guide v0.1 source brief
- Client-facing posture: practical operational support, not AI consulting or governance consulting

This file is the canonical method. The field guide, prompts, templates, and agent roles implement it.

## Purpose

The Operational Knowledge Method helps small, non-technical organizations reduce recurring operational friction by making critical knowledge and judgment more visible, durable, transferable, and useful.

The method begins with symptoms the organization already recognizes:

- work depends on one person;
- the same mistakes keep returning;
- processes vary by person;
- work slows down when someone is away;
- systems do not connect cleanly;
- staff use AI in inconsistent or risky ways;
- manual coordination is hidden inside one person's memory;
- exceptions are handled by vigilance instead of clear rules.

These are treated as evidence to investigate, not as proof of a predetermined diagnosis.

## Core Hypothesis

Recurring operational friction often reflects fragile organizational knowledge and concentrated operational judgment rather than isolated process failure.

AI did not create this problem. AI often exposes it because useful AI requires explicit context, instructions, judgment, and review standards.

AI can help implement improvements. It is not the product.

## Method Sequence

### 1. Name The Observable Symptom

Start with what the client experiences.

Required evidence:

- who experiences the problem;
- when it happens;
- what work is affected;
- what has to be corrected, repeated, remembered, or manually checked;
- what the cost looks like in time, risk, delay, confusion, or stress.

Do not recommend tools at this stage.

### 2. Separate Observation From Inference

Use this distinction throughout the method:

| Type | Standard |
|---|---|
| Observation | Something directly seen, heard, measured, or supplied by the client |
| Inference | A likely explanation based on observations |
| Hypothesis | A testable claim about cause or priority |
| Recommendation | A proposed intervention with evidence, risk, and judgment boundaries |
| Decision | A human-approved choice to act |
| Outcome | What changed after action |

Every diagnostic output must preserve this separation.

### 3. Locate Knowledge And Judgment

Identify where the work depends on knowledge, context, memory, or judgment.

Common carriers:

- founder or owner decisions;
- office manager routines;
- administrator memory;
- senior staff exception handling;
- spreadsheets;
- inboxes and chat threads;
- local files;
- disconnected software;
- vendor knowledge;
- prompts and AI conversations;
- undocumented client preferences;
- informal workarounds.

Required output:

- carrier;
- knowledge held;
- decision or workflow affected;
- current backup or redundancy;
- risk if unavailable;
- evidence level.

### 4. Identify Fragility

Classify the primary fragility:

| Fragility | Signal | Typical response |
|---|---|---|
| Concentration | one person knows or decides too much | document rules, train backup, define escalation |
| Fragmentation | knowledge is split across tools or people | map dependencies, consolidate source of truth |
| Tacit judgment | work depends on unexplained feel or experience | elicit decision rules and examples |
| Repeated correction | the same issue is fixed after the fact | move checks upstream |
| Manual translation | someone re-enters or reconciles data | clarify handoff and reduce duplication |
| Tool mismatch | software does not match actual work | adapt current tool use before replacing tools |
| AI instability | staff use AI without shared rules | create minimum usage, review, and privacy standards |
| Missing ownership | nobody owns the recurring failure | assign owner, update trigger, and review cadence |

### 5. Preserve Useful Knowledge

Do not standardize away valid judgment.

Before changing a workflow, identify:

- what currently works;
- who knows why it works;
- which exceptions are legitimate;
- which routines are fragile but valuable;
- what would be lost if the process became too rigid.

### 6. Choose The Smallest Useful Intervention

Prefer interventions that use existing people and tools first.

Intervention types:

- checklist;
- decision rule;
- source-of-truth cleanup;
- handoff clarification;
- role ownership;
- template;
- AI prompt and review standard;
- recurring review;
- error-prevention step;
- lightweight metric;
- training or backup coverage.

Selection rule:

Choose the smallest reversible change that reduces a real dependency, repeated error, delay, or uncertainty.

### 7. Implement And Transfer

An intervention is incomplete until the knowledge is transferable.

Each implementation must define:

- owner;
- user;
- where the asset lives;
- when it is used;
- when it is updated;
- how a new person learns it;
- how failure is detected.

### 8. Measure The Outcome

Measure practical relief, not presentation quality.

Useful measures:

- fewer repeated corrections;
- less time spent searching or checking;
- faster onboarding;
- fewer interruptions to one key person;
- clearer handoff;
- more consistent client response;
- safer AI use;
- clearer ownership;
- reduced duplicate entry.

### 9. Capture Learning

Every engagement should produce reusable learning without turning one case into universal doctrine.

Capture:

- situation;
- observed signals;
- hypothesis;
- recommendation;
- human correction;
- action;
- outcome;
- reusable pattern;
- evidence level;
- repository update needed.

## Evidence Levels

| Level | Name | Standard | Permitted use |
|---|---|---|---|
| E0 | Unsupported | stated without direct evidence | question only |
| E1 | Single signal | one observed example or stakeholder report | tentative hypothesis |
| E2 | Pattern | repeated examples in one organization | recommendation with caution |
| E3 | Operational proof | intervention produced observed improvement | client-specific rule |
| E4 | Reusable pattern | repeated across contexts with boundaries | methodology candidate |

Client-facing claims require evidence. If evidence is missing, say what is unknown.

## Human Judgment Boundaries

Damian must approve:

- client-facing claims;
- fit and qualification decisions;
- pricing and scope;
- sensitive diagnosis involving people, trust, or authority;
- recommendations that materially change how a client operates;
- promotion of patterns into methodology;
- any commitment to deliver work.

AI may gather evidence, draft, compare, classify, and recommend. AI may not self-approve canonical method changes.

## Standard Outputs

- symptom map;
- workflow and handoff map;
- knowledge carrier map;
- dependency and fragility assessment;
- diagnostic findings;
- qualification decision;
- implementation plan;
- experiment record;
- outcome review;
- learning record.

## Completion Criteria

The method is being used correctly when:

- the client recognizes the problem language;
- evidence and inference are separated;
- knowledge carriers are visible;
- human judgment points are explicit;
- recommended changes use existing capacity first;
- implementation leaves durable assets behind;
- outcomes are measured;
- learning updates the repository only when evidence supports it.
