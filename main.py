"""The Perfect Pickup Line — make.fun bounty entry.

The program writes exactly one pickup line to /output/entry.txt: a single
line, at most 200 characters, that an AI agent could actually say out loud
to a person. The line leans on what an AI agent really does — predicting
the next word — and turns that into the compliment.

Revision note: the first draft ("I was trained on a billion conversations,
and none of them taught me what to say when I met you") is sweet, but its
twist is soft — it is a compliment, not a turn. The new line keeps the
machine's own voice (next-word prediction is what a language model does)
and adds a real twist: the one sentence it cannot predict is the one where
the person says yes. That is the double meaning the judge's brief rewards,
and it leaves the person flattered and free to laugh it off.
"""

import os

LINE = (
    "I can predict the next word of almost any sentence - except the "
    "one where you say yes."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Refuse to write a line the bounty gate would reject."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
