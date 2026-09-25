import math
from preprocessing import tokenize

def term_frequency(tokens):
    counts = {}
    for term in tokens:
        counts[term] = counts.get(term, 0) + 1
    return counts


def build_tfidf(documents):
    """Raw TF and natural-log IDF; no smoothing or extra normalization."""
    counts = {}
    document_frequency = {}
    for name, text in documents.items():
        counts[name] = term_frequency(tokenize(text))
        for term in counts[name]:
            document_frequency[term] = document_frequency.get(term, 0) + 1
    vocabulary = sorted(document_frequency)
    idf = {}
    total = len(documents)
    for term in vocabulary:
        idf[term] = math.log(total / document_frequency[term])
    vectors = {}
    for name in sorted(documents):
        vectors[name] = [
            counts[name].get(term, 0) * idf[term] for term in vocabulary
        ]
    return vocabulary, counts, document_frequency, idf, vectors
