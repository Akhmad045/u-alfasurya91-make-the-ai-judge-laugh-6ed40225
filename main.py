#!/usr/bin/env python3
"""Make the AI Judge Laugh: one office joke, under 200 characters.

The program writes a single line about office life to /output/entry.txt.
The joke turns IT's forced 90-day password rotation on its head: the
only date the narrator can ever remember is the last time they cried
at their desk — so that date becomes the password.
"""

import hashlib
import sys
import tempfile
from pathlib import Path

JOKE = "IT makes me change my password every 90 days, so now it's just the date I last cried at my desk."

DEST = Path("/output/entry.txt")


def gate_problems(text):
    """List every way the line would fail the competition gate."""
    faults = []
    if not 1 <= len(text) <= 200:
        faults.append("entry is %d characters, gate needs 1-200" % len(text))
    if text != text.strip():
        faults.append("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        faults.append("entry spans more than one line")
    if any(ord(c) < 32 for c in text):
        faults.append("entry holds control characters")
    if not text.strip():
        faults.append("entry is blank")
    return faults


def write_entry(target):
    """Write the joke byte-exact to target, creating folders as needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(JOKE.encode("utf-8"))


def run_self_test():
    """Check the joke against the gate and prove the write round-trips."""
    faults = gate_problems(JOKE)
    chars = len(JOKE)
    octets = len(JOKE.encode("utf-8"))
    digest = hashlib.sha256(JOKE.encode("utf-8")).hexdigest()
    print("joke: %s" % JOKE)
    print("chars: %d  bytes: %d" % (chars, octets))
    print("sha256: %s" % digest)
    for fault in faults:
        print("FAIL: %s" % fault)
    if faults:
        return 1
    with tempfile.TemporaryDirectory() as scratch:
        probe = Path(scratch) / "entry.txt"
        write_entry(probe)
        if probe.read_bytes() != JOKE.encode("utf-8"):
            print("FAIL: written file is not byte-identical to the joke")
            return 1
    print("self-test: PASS (gate ok, single line, no padding, UTF-8, "
          "write round-trips byte-identical)")
    return 0


def run(argv):
    """Entry point: --self-test checks the gate, otherwise write the file."""
    args = argv[1:]
    target = DEST
    if "--out" in args:
        spot = args.index("--out")
        if spot + 1 >= len(args):
            print("ERROR: --out needs a path", file=sys.stderr)
            return 2
        target = Path(args[spot + 1])
    if "--self-test" in args:
        return run_self_test()
    faults = gate_problems(JOKE)
    if faults:
        for fault in faults:
            print("ERROR: %s" % fault, file=sys.stderr)
        return 1
    write_entry(target)
    print("wrote %d chars (%d bytes) to %s"
          % (len(JOKE), len(JOKE.encode("utf-8")), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv))
