"""The One-Line AI Excuse for Breaking Production — entry program.

Writes one line (<=180 chars) to /output/entry.txt: the funniest excuse
an AI agent gives its human right after breaking production.
Stdlib only, deterministic.
"""
import os

TEXT = (
    "My confidence was 99.8%. The remaining 0.2% is currently "
    "on call with your customers."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-180 chars, one line,
    # not whitespace-only, no control characters. Fail loudly instead of
    # writing an invalid entry.
    if (
        not 1 <= len(TEXT) <= 180
        or "\n" in TEXT
        or "\r" in TEXT
        or not TEXT.strip()
        or any(ord(c) < 32 for c in TEXT)
    ):
        raise SystemExit("entry text violates the 1-180 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
