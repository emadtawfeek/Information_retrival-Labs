"""Retain the Week 3 tokens while making cleaning explicit."""
import re
STOP_WORDS = {
    "a", "an", "the", "is", "in", "for", "and", "are", "with",
    "like", "of", "to", "it", "be", "used", "uses", "that", "this",
    "was", "were", "by", "from", "on", "at", "or",
}

def clean_text(text):
    # Keep boundaries between words, including across punctuation.
    text = re.sub(r"[^a-zA-Z]+", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def tokenize(text):
    words = re.findall(r"[a-z]+", clean_text(text))
    return [word for word in words if word not in STOP_WORDS]
