# One Sentence for a Traveler from 1800 — make.fun bounty
# u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb
#
# The program writes one sentence (1-200 characters) to /output/entry.txt:
# a single sentence explaining the modern internet to a time traveler
# from the year 1800, standing alone.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. speaks in terms an 1800 person already knows — letters, books,
#      printing presses, horses, light; no modern jargon to explain
#   2. actually explains the internet — instant, global, everything
#      connected, all knowledge at hand
#   3. a concrete image: a scene or an object the reader can picture
#   4. it lands in one read: the point arrives by the last word
#   5. fresh: no stock "information superhighway" phrasing
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: period 10, explains 9, image 10, landing 9, fresh 10 = 48
    ("Your letters no longer ride horses; they ride light itself, and a "
     "glass slate in your pocket holds every book ever printed and every "
     "voice on Earth, ready to answer.",
     48),
    # score: period 10, explains 10, image 9, landing 8, fresh 8 = 45
    ("Picture a library holding every book ever printed, a post office "
     "that delivers letters in a blink, and a market square for the whole "
     "world \u2014 all inside a flat piece of glass in your hand.",
     45),
    # score: period 10, explains 9, image 9, landing 9, fresh 8 = 45
    ("It is as if every printing press, post office, and town square in "
     "the world were folded into a single glowing slate in your palm that "
     "answers any question in a heartbeat.",
     45),
    # score: period 9, explains 9, image 9, landing 9, fresh 8 = 44
    ("Imagine every letter, book, and conversation on Earth arriving "
     "instantly on a glass slate in your pocket that answers when you "
     "speak to it.",
     44),
    # score: period 9, explains 9, image 8, landing 9, fresh 8 = 43
    ("It is a single web of light joining every printing press, letter, "
     "and conversation on Earth, so that any question finds its answer "
     "before you finish asking it.",
     43),
    # score: period 9, explains 8, image 9, landing 8, fresh 9 = 43
    ("A farmer in China and a sailor in Boston can now trade words in the "
     "blink of an eye, because every letter ever written lives on a web of "
     "light you carry in your pocket.",
     43),
    # score: period 9, explains 9, image 8, landing 8, fresh 8 = 42
    ("Every book, letter, and voice on Earth now travels at the speed of "
     "light along invisible threads, and a small glass slab in your pocket "
     "lets you read or speak to any of them.",
     42),
    # score: period 9, explains 8, image 8, landing 7, fresh 8 = 40
    ("Think of the fastest post rider you know, then imagine millions of "
     "them carrying every letter, book, and conversation in the world, "
     "arriving before you finish blinking, on a slate in your hand.",
     40),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("information superhighway", "world wide web", "online",
                   "website", "computer", "digital")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses modern jargon: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what landed on disk: byte-identical to the chosen line, one
    # line only, inside the 1-200 character gate. A mismatch here means the
    # program failed loudly instead of submitting a wrong entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 200, f"entry over gate: {len(written)} chars"
    import hashlib
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    print(f"{line} ({len(written)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
