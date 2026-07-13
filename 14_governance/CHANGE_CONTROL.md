# Change Control

## Change classes

### Methodology

Requires:

- evidence;
- impact analysis;
- explicit approval;
- version increment;
- affected module review.

### Procedure

Requires:

- observed operational need;
- owner review;
- changelog entry.

### Prompt

Requires:

- test case;
- before-and-after comparison;
- output validation;
- version increment.

### Messaging

May change rapidly, but field evidence must be captured.

### Generated artifact

Never edited directly.

## Traceability rule

Every canonical rule must trace to one of:

- approved strategic conclusion;
- operational requirement;
- observed evidence;
- explicit governance decision.

Conversation alone is not authority.

## Canonical Ownership Rule

Each reusable method, prompt, template, definition, or decision rule has one owner file. Other files reference the owner instead of restating the asset.

## Generated Artifact Rule

Files under `build/` and packaged archives are derivative. They may be regenerated from source and must not be edited as canonical source.

## Version Rule

Use semantic repository versions in `CURRENT_STATE.md` and dated changelog entries. A version changes when repository capability changes, not when a generated artifact is rebuilt.
