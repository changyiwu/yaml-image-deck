#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import yaml

root = Path(__file__).resolve().parents[1]
skill = root / "skills" / "yaml-image-deck"

text = (skill / "SKILL.md").read_text(encoding="utf-8")
if not text.startswith("---\n") or "name: yaml-image-deck" not in text:
    raise SystemExit("Invalid SKILL.md frontmatter")

interface = yaml.safe_load((skill / "agents" / "interface.yaml").read_text(encoding="utf-8"))
prompt = interface.get("interface", {}).get("default_prompt", "")
if "yaml-image-deck" not in prompt:
    raise SystemExit("agents/interface.yaml default_prompt must mention yaml-image-deck")

result = subprocess.run([
    sys.executable,
    str(skill / "scripts" / "validate_spec.py"),
    "--spec",
    str(skill / "assets" / "spec-template.yaml"),
])
raise SystemExit(result.returncode)

