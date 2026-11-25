#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger -- make.fun entry (Account B).

The program writes one line of plain text (at most 200 characters) to
/output/entry.txt: the phone battery's final message to the charger it
waited for all day.

Premise: the battery texts its charger from the recycling bin -- the
afterlife. It forgives the charger, but warns the next battery about
the "just five more minutes" lie.

How the line maps to the judge's brief (most important first):
1. On-subject: it is the battery's last text to its charger, one line,
   sent from the recycling bin -- the afterlife, so it is literally a
   last text.
2. Real joke with a turn: the setup forgives the charger, then the
   final words flip it -- "that's the lie that killed me" -- the
   charger's own "five more minutes" is the murder weapon.
3. A person's voice: lowercase, texting shorthand, needy and a little
   spiteful ("i forgive you" followed at once by a warning).
4. Spends its characters: every clause earns the punchline -- bin,
   forgiveness, favour, the begging, the lie, the death -- no filler.
5. Beyond the obvious dying-battery complaint: not "I'm at 1%", but a
   post-mortem grudge and a warning to the replacement; funny again on
   a second read, when "the lie" lands as the cause of death.
"""

import os

ENTRY = (
    "hey, it's me, texting from the recycling bin. i forgive you. "
    "do the next battery one favour: when it begs for "
    "'five more minutes', tell it that's the lie that killed me."
)

MAX_CHARS = 200


def write_entry(path="/output/entry.txt"):
    """Validate the entry against the gate and write it to ``path``.

    Gate (RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200
    characters, not only white space, one line.
    """
    text = ENTRY
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, gate needs 1 to %d"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # gate requires UTF-8 text
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return text


if __name__ == "__main__":
    written = write_entry()
    print("wrote %d characters to /output/entry.txt" % len(written))
    print(written)
