"""Build the files you hand to Muse and the website, filling in your details from muse/MEMORY.md.

    python3 scripts/build.py

Outputs (in build/):
  MUSE-PASTE-PACK.md   everything Muse needs in one file, in paste order
  site/index.html      the one-page website for your domain
  Pipeline.xlsx        run scripts/build_pipeline_xlsx.py for this one
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MUSE = ROOT / "muse"
OUT = ROOT / "build"

FIELDS = ["owner_name", "business_name", "domain", "sending_inbox", "physical_address",
          "timezone", "payment_link", "drive_folder", "pipeline_sheet"]


def read_memory_fields():
    text = (MUSE / "MEMORY.md").read_text()
    values = {}
    for field in FIELDS:
        m = re.search(rf"^- {field}: (.+)$", text, re.M)
        raw = m.group(1).strip() if m else "FILL_ME"
        # Drop trailing hints like "(e.g. ...)" or "(confirm, ...)"
        values[field] = re.sub(r"\s*\(.*\)\s*$", "", raw) or "FILL_ME"
    return values


def fill(text, values):
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def section(title, path):
    return f"\n\n---\n\n# FILE: {title}\n\n" + path.read_text().strip() + "\n"


def build_paste_pack(values):
    parts = [
        "# Muse paste pack\n\n"
        "Paste or upload in this order. Part 1 goes in Muse's soul/persona file, part 2 in its memory file, "
        "and the rest are reference files (or a `## Playbooks` section in memory if Muse has no file upload).\n"
        "The full humanizer skill is in muse/skills/humanizer/ (upload SKILL.md and the voice profile separately).",
        section("1. SOUL (persona file)", MUSE / "SOUL.md"),
        section("2. MEMORY (memory file)", MUSE / "MEMORY.md"),
        section("3. ROUTINES (create these as scheduled tasks)", MUSE / "ROUTINES.md"),
    ]
    for p in sorted((MUSE / "playbooks").glob("*.md")):
        parts.append(section(f"playbooks/{p.name}", p))
    for p in sorted((MUSE / "templates").glob("*.md")):
        parts.append(section(f"templates/{p.name}", p))
    OUT.mkdir(exist_ok=True)
    out = OUT / "MUSE-PASTE-PACK.md"
    out.write_text(fill("".join(parts), values))
    return out


def build_site(values):
    src = (ROOT / "site" / "index.html").read_text()
    out = OUT / "site" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(fill(src, values))
    return out


def main():
    values = read_memory_fields()
    for path in (build_paste_pack(values), build_site(values)):
        print("wrote", path.relative_to(ROOT))
    missing = [k for k, v in values.items() if v.startswith("FILL_ME")]
    if missing:
        print("\nStill FILL_ME in muse/MEMORY.md:", ", ".join(missing))
        print("Fill those in and run this again before uploading to Muse or publishing the site.")
        sys.exit(1)


if __name__ == "__main__":
    main()
