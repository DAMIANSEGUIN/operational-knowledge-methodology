from pathlib import Path
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
    "02_gap_analysis/GAP_ANALYSIS_TEMPLATE.md",
    "11_agents/AGENTS.md",
    "14_governance/CHANGE_CONTROL.md",
]

missing = [p for p in required if not (ROOT / p).exists()]

if missing:
    print("Repository validation failed.")
    for item in missing:
        print(f"Missing: {item}")
    sys.exit(1)

print("Repository validation passed.")
