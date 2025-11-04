import sys
import pathlib

def stats(path: str):
    chars = words = lines = 0
    for p in pathlib.Path(path).rglob("*.py"):
        text = p.read_text(encoding="utf-8")
        chars += len(text)
        words += len(text.split())
        lines += text.count("\n") + (1 if text else 0)
    return chars, words, lines


if __name__ == "__main__":
    # Allow an argument like: python tools/count_stats.py src
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    c, w, l = stats(base)
    print(f"chars={c}, words={w}, lines={l}")

    # Optional quality gate example (can cause CI fail if too big)
    if l > 2000:
        raise SystemExit("Too many lines; consider refactoring.")
