# Operational Knowledge Methodology

## Project authority

This repository is the canonical source for the methodology, field guide, prompts, operating rules, and reusable assets used to diagnose and improve operational problems in small and medium-sized organizations.

The repository serves two purposes:

1. Produce a client-facing and agent-executable field guide for identifying, approaching, diagnosing, qualifying, and helping organizations.
2. Provide a structured implementation environment that Claude, Codex, ChatGPT, and future agents can use without relying on conversation history.

## Primary objective

Help small, non-technical organizations solve operational and strategic problems by identifying where critical organizational knowledge and operational judgment reside, where they are concentrated or fragmented, how they are protected, and how they can be made more durable, transferable, and useful.

## Client-facing symptoms

The methodology begins with problems the client already recognizes:

- Why does everything depend on one person?
- Why are we constantly fixing the same mistakes?
- Why are our processes inconsistent?
- Why does work slow down whenever someone is away?
- Why do we have five systems that do not talk to each other?
- Why does every employee use AI differently?

These are treated as symptoms, not isolated failures.

## Working hypothesis

Recurring operational friction often reflects fragmented organizational judgment and weak knowledge transfer rather than isolated process defects.

AI did not create the underlying problem. AI frequently exposes it by forcing organizations to make implicit knowledge explicit.

## Market position

Do not lead with AI, governance, knowledge sovereignty, or architecture.

Lead with recognizable operational problems.

AI is an optional implementation capability, not the product.

The service promise remains simple:

> I help small organizations remove operational friction using the people and tools they already have.

## Core commercial model

- Target: organizations with roughly 5–30 employees
- No software engineering team
- No mature operations function
- Limited internal AI expertise
- Existing tools are underused, disconnected, or inconsistently applied
- Engagement model: approximately three hours per week on a fixed monthly retainer
- Goal: 3–5 retained clients
- Method: small, continuous improvements rather than large transformation projects

## Current dependency order

1. Reverse Information Paradox Strategic Review asks whether the methodology should change.
2. Operations Support Gap Analysis determines what should change.
3. Revised Field Manual implements approved changes.
4. Repository implementation operationalizes the approved methodology.
5. Broader constitutional architecture is considered only if the approved methodology generates rules that generalize beyond Operations Support.

Do not reverse this order.

## Non-negotiable operating rules

- Diagnose before prescribing.
- Treat operational symptoms as evidence.
- Identify where critical knowledge and judgment are carried.
- Separate observed evidence from inference.
- Preserve valid knowledge, not existing structure.
- Prefer existing people and tools before adding new systems.
- Do not recommend software before understanding the operational problem.
- Keep external messaging simple.
- Keep internal intelligence rigorous.
- Do not optimize persuasion over truth.
- Every recommendation must identify assumptions, evidence, risks, and required human judgment.
- No rule becomes canonical solely because it appeared in a conversation or was proposed by an AI.
- Every reusable asset has one canonical owner.
- Generated artifacts are not canonical sources.
- Repository state must be recoverable without conversation history.

## Human and AI roles

### AI team

- Lead research
- Detect patterns
- Diagnose operational and knowledge dependencies
- Generate solution options
- Produce qualification packages
- Prepare client-facing language
- Measure outcomes
- Capture learning
- Maintain repository coherence

### Damian

- Calibrate messaging for specific leads
- Judge fit, timing, trust, and commercial commitments
- Approve client-facing claims
- Select among context-sensitive options
- Correct agent recommendations
- Provide rationale when correction contains a reusable decision boundary

## Learning model

The system improves through structured evidence:

1. Situation
2. Observed signals
3. AI diagnosis
4. AI recommendation
5. Human decision or correction
6. Reason for correction
7. Action taken
8. Outcome
9. Reusable rule or pattern
10. Required repository update

Agreement is not sufficient evidence of learning. Explained disagreement is the primary source of calibration.

## Agent startup protocol

Before performing project work:

1. Read `PROJECT.md`.
2. Read `CURRENT_STATE.md`.
3. Read the relevant module index.
4. Identify the canonical file to edit.
5. Do not create a new file if an existing canonical owner already exists.
6. Produce the requested artifact.
7. Update `CURRENT_STATE.md`.
8. Update `CHANGELOG.md`.
9. Record unresolved decisions in `DECISIONS.md`.

## Definition of done

A module is complete only when:

- purpose is explicit;
- inputs and outputs are defined;
- decision rules are executable;
- human judgment points are identified;
- failure modes are documented;
- canonical prompts and templates exist;
- metrics are defined;
- learning capture is wired back into the repository.
