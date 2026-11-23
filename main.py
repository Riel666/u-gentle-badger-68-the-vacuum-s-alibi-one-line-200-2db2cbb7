"""Write one line to /output/entry.txt.

A robot vacuum explains why it missed a spot: the spot was
scanned, classified as load-bearing dust, and left in place for
structural reasons. Deadpan, at most 200 characters, and the
program writes exactly that line and nothing else.
"""

import os

ENTRY = "I scanned the spot, classified it as 'load-bearing dust', and left it in place for structural reasons."


def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY == ENTRY.strip()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
