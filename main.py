#!/usr/bin/env python3
"""Make the AI Judge Laugh (office life) — make.fun entry.

Writes one single-line joke about office life (at most 200 characters)
to /output/entry.txt. The joke is a true office observation with a
surprising last word: forced 90-day password rotation meets the date
of the last desk cry.
"""

import argparse
import sys
from pathlib import Path

ENTRY = (
    "IT makes me change my password every 90 days, so now it's just "
    "the date I last cried at my desk."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> list[str]:
    """Check the gate: UTF-8 text, 1-200 chars, single line, no padding."""
    problems = []
    if not (1 <= len(text) <= 200):
        problems.append(f"length {len(text)} chars, must be 1-200")
    if not text.strip():
        problems.append("entry is only whitespace")
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry is not a single line")
    # Control characters (tabs, bells, ...) would break the one-breath
    # read-aloud, so the gate rejects them even though they are UTF-8.
    if any(ord(ch) < 32 for ch in text):
        problems.append("entry contains control characters")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover - defensive
        problems.append(f"not valid UTF-8: {exc}")
    return problems


def self_test() -> int:
    """Validate the entry against the gate and report the result."""
    import hashlib
    import tempfile

    problems = validate(ENTRY)
    chars = len(ENTRY)
    nbytes = len(ENTRY.encode("utf-8"))
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"entry: {ENTRY}")
    print(f"chars: {chars}  bytes: {nbytes}")
    print(f"sha256: {digest}")
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        return 1
    # Round-trip check: the file the program writes must read back
    # byte-identical, with no trailing newline added.
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "entry.txt"
        probe.write_text(ENTRY, encoding="utf-8")
        if probe.read_bytes() != ENTRY.encode("utf-8"):
            print("FAIL: written file does not round-trip byte-identical")
            return 1
    print("self-test: PASS (1-200 chars, single line, no padding, UTF-8, "
          "round-trip byte-identical)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="validate the entry against the gate and exit")
    parser.add_argument("--out", type=Path, default=OUTPUT_PATH,
                        help="where to write entry.txt (default: /output/entry.txt)")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars ({len(ENTRY.encode('utf-8'))} bytes) "
          f"to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
