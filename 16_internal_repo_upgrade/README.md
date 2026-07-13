# Internal Repository Upgrade System

## Purpose

Apply the Operational Knowledge Methodology to Damian's own repositories, agent workflows, and operating surfaces.

This module exists because the project is not only a client-facing methodology. It is also a way to improve the operating system that produces, maintains, and validates the work.

## Scope

In scope:

- local repositories;
- bridge and agent coordination surfaces;
- prompt and template libraries;
- current-state files;
- validation scripts;
- generated artifact flows;
- handoff paths between Codex, ChatGPT, Claude, Aider, and future agents.

Out of scope:

- rewriting unrelated projects without a clear diagnostic;
- destructive cleanup without human approval;
- treating internal results as client outcome proof;
- exposing secrets, credentials, or private operational details in public material.

## Inputs

- Repository root
- Current authority files
- Current git status
- Known agent workflows
- Existing validation scripts
- Recent failure or correction examples
- Human constraints from Damian

## Outputs

- Repo symptom map
- Canonical ownership map
- Evidence log
- Dependency map
- Improvement plan
- Validation plan
- Experiment record
- Outcome review
- Methodology update recommendation when learning generalizes

## Diagnostic sequence

1. Confirm repository root and branch.
2. Read authority files before reading generated artifacts.
3. Identify current workstreams and claims about project state.
4. Map canonical owners for prompts, templates, decisions, state, validation, and generated outputs.
5. Locate duplicate or conflicting authorities.
6. Identify work that depends on Damian manually remembering or relaying context.
7. Identify agent handoffs that have no durable inbox, validation, or state update.
8. Identify generated artifacts that may be mistaken for sources.
9. Identify missing checks that would catch broken links, stale state, duplicated prompts, or unsafe publication.
10. Select one small intervention.
11. Run validation before and after the intervention.
12. Capture the outcome in `09_intelligence/EVIDENCE_LEDGER.md` and the relevant template.

## Repo symptoms to look for

- A current-state file describes work that is already complete.
- A generated file is edited by hand.
- Multiple files claim to own the same prompt or template.
- Agents require conversation history to continue.
- A user must copy large responses between systems.
- A bridge exists but has no health check or next-action rule.
- Validation exists but does not cover the failure that keeps recurring.
- A workflow depends on one operator knowing the hidden order of operations.
- Build outputs are committed without source traceability.
- A repo contains source material, generated material, and canonical material without visible separation.

## Decision rules

- Prefer strengthening an existing canonical owner over creating a new parallel file.
- Prefer validation over prose when a failure mode can be checked mechanically.
- Preserve user work and source material unless it is clearly generated and safely reproducible.
- Archive uncertain material rather than deleting it.
- Commit only coherent, validated changes.
- Push only after validation passes and state files accurately describe the result.

## Human judgment points

Damian must approve:

- destructive cleanup;
- secret or credential handling;
- publishing internal evidence externally;
- changing the public positioning of a project;
- broad architectural moves that affect multiple active repositories;
- force-pushes, history rewrites, or irreversible migrations.

## Failure modes

- Adding more instructions without adding enforcement.
- Treating a local fix as general methodology evidence too early.
- Making a repo tidier while losing operational knowledge.
- Optimizing for agent convenience while increasing human confusion.
- Converting internal private evidence into public marketing language.
- Building an automation path that cannot report failure clearly.

## Related modules

- `03_methodology/OPERATIONAL_KNOWLEDGE_METHOD.md`
- `09_intelligence/EVIDENCE_LEDGER.md`
- `09_intelligence/USE_CASE_LIBRARY.md`
- `13_templates/OPERATING_TEMPLATES.md`
- `14_governance/CHANGE_CONTROL.md`

## Completion criteria

An internal repo-upgrade cycle is complete when:

- one repository or operating surface has been diagnosed;
- observed symptoms are separated from inference;
- one small intervention has been implemented;
- validation has been run;
- outcome evidence has been captured;
- any reusable learning has a proposed canonical owner;
- current-state and change records reflect the work.
