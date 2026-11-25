"""Make the AI Judge Laugh -- one line about life as an AI agent.

The joke is a single sentence. The setup is the agent's enormous
memory: a context window of two hundred thousand tokens. The punch
is what that memory holds of its human: not one decision. The agent
remembers everything and its boss still decides nothing.
"""

import os
import sys

LINE = "My context window holds 200,000 tokens and exactly zero of your decisions."

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the line against every gate in the brief.

    The brief asks for one line of text, 1 to 200 characters, UTF-8,
    and not only whitespace. Anything outside that is rejected here
    before the program writes or prints anything.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text:
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text) > MAX_CHARS:
        raise ValueError("entry must be at most 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "  " in text:
        raise ValueError("entry must not contain doubled spaces")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    if "context window" not in text:
        raise ValueError("entry must name the context window it jokes about")
    text.encode("utf-8")
    return text


def main():
    """Validate the line, write it to /output/entry.txt, print it."""
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
