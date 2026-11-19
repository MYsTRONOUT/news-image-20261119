"""news-image-20261119 entry program (Python 3.13, stdlib only).

Ships the entry image beside this file and copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). No network, no clock,
no randomness: two runs write identical bytes.

Run locally with MAKEFUN_OUTPUT_DIR=out python3 main.py after mkdir -p out.
"""

import hashlib, os, shutil, sys
import pathlib

SRC = pathlib.Path(__file__).resolve().parent / "entry.png"


def digest(path):
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def run():
    # One straight copy and a hash comparison; nothing varies between runs.
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.png"
    shutil.copyfile(SRC, target)
    if digest(target) != digest(SRC):
        print("error: copy mismatch", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


run()
