from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "PROJECT.md",
    "CURRENT_STATE.md",
    "README.md",
    "CHANGELOG.md",
    "DECISIONS.md",
    "GLOSSARY.md",
    "01_strategic_review/STRATEGIC_REVIEW.md",
    "02_gap_analysis/GAP_ANALYSIS_v1.md",
    "02_gap_analysis/GAP_ANALYSIS_TEMPLATE.md",
    "03_methodology/OPERATIONAL_KNOWLEDGE_METHOD.md",
    "04_field_guide/README.md",
    "05_diagnostic/README.md",
    "06_qualification/README.md",
    "07_translation/README.md",
    "08_implementation/README.md",
    "09_intelligence/README.md",
    "10_campaign/README.md",
    "11_agents/AGENTS.md",
    "12_prompts/README.md",
    "13_templates/DECISION_PACKET.md",
    "13_templates/LEARNING_RECORD.md",
    "13_templates/OPERATING_TEMPLATES.md",
    "14_governance/CHANGE_CONTROL.md",
    "14_governance/VALIDATION_CHECKLIST.md",
    "15_source_material/README.md",
    "15_source_material/Operations_Support_Field_Guide_v0_1.md",
    "15_source_material/Operations_Support_Field_Guide_v0_1.docx",
]

module_dirs = [
    "00_orientation",
    "01_strategic_review",
    "02_gap_analysis",
    "03_methodology",
    "04_field_guide",
    "05_diagnostic",
    "06_qualification",
    "07_translation",
    "08_implementation",
    "09_intelligence",
    "10_campaign",
    "11_agents",
    "12_prompts",
    "13_templates",
    "14_governance",
    "15_source_material",
]

placeholder_re = re.compile(r"\b(TODO|TBD|lorem ipsum|placeholder)\b", re.IGNORECASE)
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def markdown_files():
    return [
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and "build" not in p.parts
    ]


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for match in link_re.finditer(text):
        target = match.group(1).strip()
        if (
            target.startswith(("http://", "https://", "mailto:", "#"))
            or "://" in target
        ):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        if not (path.parent / clean).resolve().exists():
            errors.append(f"Broken link in {path.relative_to(ROOT)} -> {target}")


def main() -> int:
    errors: list[str] = []

    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required file: {rel}")

    for rel in module_dirs:
        if not (ROOT / rel).is_dir():
            errors.append(f"Missing module directory: {rel}")

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if placeholder_re.search(text):
            errors.append(f"Placeholder marker in {path.relative_to(ROOT)}")
        validate_links(path, errors)

    prompt_headings = []
    prompt_text = (ROOT / "12_prompts/README.md").read_text(encoding="utf-8")
    for line in prompt_text.splitlines():
        if line.startswith("## ") and "Prompt" in line:
            prompt_headings.append(line.strip())
    duplicates = sorted({p for p in prompt_headings if prompt_headings.count(p) > 1})
    for item in duplicates:
        errors.append(f"Duplicate prompt heading: {item}")

    if errors:
        print("Repository validation failed.")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
