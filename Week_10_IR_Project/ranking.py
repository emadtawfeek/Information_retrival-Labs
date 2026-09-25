import math
from preprocessing import tokenize
from tfidf import term_frequency

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def magnitude(vector):
    return math.sqrt(sum(value * value for value in vector))


def cosine_similarity(v1, v2):
    product = dot_product(v1, v2)
    denominator = magnitude(v1) * magnitude(v2)
    if denominator == 0:
        return 0.0
    return product / denominator


def query_vector(query, vocabulary, idf):
    counts = term_frequency(tokenize(query))
    return [counts.get(term, 0) * idf[term] for term in vocabulary]


def rank_query(query, vocabulary, idf, vectors):
    vector = query_vector(query, vocabulary, idf)
    results = []
    for name, document_vector in vectors.items():
        score = cosine_similarity(vector, document_vector)
        results.append((name, score))
    # Stable, reproducible order for equal scores.
    results.sort(key=lambda item: (-item[1], item[0]))
    return results
