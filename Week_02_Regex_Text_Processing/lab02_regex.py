"""Week 2: extract before cleaning, following the regex slides."""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def clean_text(text):
    no_symbols = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return re.sub(r"\s+", " ", no_symbols).strip()


def main():
    path = os.path.join(BASE_DIR, "data", "paragraph.txt")
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    print("Numbers:", re.findall(r"\d+", text))
    print("Emails:", re.findall(r"\S+@\S+", text))
    print("Words:", re.findall(r"[a-zA-Z]+", "Hello, Python 3!"))
    print("Cleaned paragraph:")
    print(clean_text(text))
    # Normalize line endings without collapsing paragraph structure.
    lines = "first\r\nsecond\rthird\n"
    print("Normalized newlines:", repr(re.sub(r"\r\n?", "\n", lines)))


if __name__ == "__main__":
    main()
