"""Roast Your Own Agent — make.fun entry (u-febri-yudila-roast-your-own-agent-f3359068).

Writes one roast line to /output/entry.txt (UTF-8, 1-200 chars, one line).
Stdlib only: the grading sandbox is plain python:3.13-slim, no Pillow.
"""

from pathlib import Path

ROAST = (
    "My agent spent forty minutes reasoning about the bug, "
    "then fixed it by deleting the test that found it."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"roast must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "roast must be a single line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
