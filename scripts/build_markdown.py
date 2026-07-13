from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "OPERATIONS_SUPPORT_FIELD_GUIDE.md"

order = [
    "00_orientation/CLIENT_SUMMARY.md",
    "00_orientation/SYSTEM_ORIENTATION.md",
    "01_strategic_review/STRATEGIC_REVIEW.md",
    "02_gap_analysis/GAP_ANALYSIS_v1.md",
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
    "13_templates/OPERATING_TEMPLATES.md",
    "13_templates/DECISION_PACKET.md",
    "13_templates/LEARNING_RECORD.md",
    "14_governance/CHANGE_CONTROL.md",
]

parts = []
for rel in order:
    path = ROOT / rel
    if path.exists():
        parts.append(path.read_text(encoding="utf-8").strip())

OUT.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
print(OUT)
