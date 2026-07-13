# Use Case Library

## Purpose

Translate research, internal observations, and field evidence into reusable use cases that can guide diagnostics, outreach, implementation, and evidence capture.

Each use case must connect a recognizable symptom to evidence, questions, small interventions, and proof metrics.

## Use case format

- Symptom
- Likely operational mechanism
- Evidence to gather
- Diagnostic questions
- Small intervention
- Proof metric
- Failure mode
- Related templates

## UC-001 — Key-person dependency

- Symptom: Work slows down, decisions stall, or mistakes increase when one person is absent.
- Likely operational mechanism: Critical knowledge and judgment live in one person's memory, inbox, habits, or private files.
- Evidence to gather: absence workarounds, recurring escalations, shadow instructions, undocumented exceptions, repeated Slack or email questions.
- Diagnostic questions: "Who gets interrupted when this work gets stuck?" "What does that person know that others do not?" "Which decisions cannot be made from the written process?"
- Small intervention: Document the judgment points, create a dependency map, write a lightweight decision guide, and test it with another person.
- Proof metric: Fewer escalations to the key person for the same workflow.
- Failure mode: Capturing steps without capturing judgment.
- Related templates: dependency map, workflow map, evidence log, outcome review.

## UC-002 — Repeated correction loops

- Symptom: The same mistake is corrected repeatedly, often by the same reviewer or manager.
- Likely operational mechanism: The process lacks a clear quality standard, feedback loop, or ownership point.
- Evidence to gather: examples of repeated corrections, reviewer notes, rework time, unclear approval criteria.
- Diagnostic questions: "What keeps getting corrected?" "Where should the mistake have been caught?" "Does the person doing the work know the standard before submitting it?"
- Small intervention: Convert corrections into a visible checklist or decision rule and review the next three instances.
- Proof metric: Fewer repeated corrections for the same issue.
- Failure mode: Treating the person as the problem when the standard is invisible.
- Related templates: human correction record, experiment record, outcome review.

## UC-003 — Disconnected systems and manual reconciliation

- Symptom: Staff copy information between tools, reconcile conflicting records, or maintain side spreadsheets.
- Likely operational mechanism: Tool boundaries are unclear, systems do not share a source of truth, or ownership is missing.
- Evidence to gather: duplicate records, manual copy steps, reconciliation notes, missed handoffs, conflicting fields.
- Diagnostic questions: "Where is the source of truth?" "Who checks whether the records match?" "Which system wins when two systems disagree?"
- Small intervention: Define one source of truth for a narrow workflow and remove one duplicate entry step.
- Proof metric: Fewer manual reconciliation steps and fewer mismatched records.
- Failure mode: Buying another tool before clarifying ownership and source-of-truth rules.
- Related templates: workflow map, dependency map, implementation plan.

## UC-004 — Inconsistent AI use

- Symptom: Employees use AI differently, produce inconsistent output, or rely on AI without shared review rules.
- Likely operational mechanism: AI is being used inside weak workflows where quality standards and source authority are already unclear.
- Evidence to gather: examples of AI-generated work, review practices, prompt reuse, tool access, errors, manager expectations.
- Diagnostic questions: "Which tasks are people using AI for?" "Who reviews AI output?" "What sources are considered authoritative?" "What work should not be delegated to AI?"
- Small intervention: Define approved uses, review rules, source-checking expectations, and one reusable prompt for a narrow workflow.
- Proof metric: More consistent AI-assisted output and fewer unreviewed AI decisions.
- Failure mode: Writing a broad AI policy before understanding actual work.
- Related templates: evidence log, decision packet, human correction record.

## UC-005 — Onboarding dependence

- Symptom: New staff require repeated live explanation, and performance depends on who trained them.
- Likely operational mechanism: Training depends on memory, informal demonstration, and local exceptions rather than durable workflow knowledge.
- Evidence to gather: onboarding questions, repeated training topics, undocumented exceptions, inconsistent instructions from different trainers.
- Diagnostic questions: "What does a new person need to ask twice?" "Which parts of training depend on the trainer?" "Where do exceptions live?"
- Small intervention: Capture the first complete workflow, its judgment points, and the most common exceptions, then use it in the next onboarding moment.
- Proof metric: Fewer repeat questions and faster independent completion of the workflow.
- Failure mode: Creating a large manual no one maintains.
- Related templates: workflow map, evidence log, outcome review.

## UC-006 — Internal repository and agent workflow upgrade

- Symptom: A repository, agent workflow, or operating surface requires manual relay, repeated correction, stale state files, or unclear authority before work can proceed.
- Likely operational mechanism: The repository lacks durable control surfaces, validation, ownership, or a reliable path from instruction to executed change.
- Evidence to gather: stale current-state claims, duplicate prompts, generated artifacts treated as sources, manual copy/paste handoffs, failed validation, missing decision records.
- Diagnostic questions: "Which file is authoritative?" "What work depends on Damian remembering context?" "Which check would catch drift before a user sees it?" "Where does another agent need to write or read safely?"
- Small intervention: Establish canonical ownership, add validation, update state files, and test a small agent-executed change.
- Proof metric: Fewer manual relays and a cleaner path from instruction to validated repo change.
- Failure mode: Adding more instructions without enforcement, validation, or next-action routing.
- Related templates: methodology decision record, evidence log, experiment record, outcome review.
