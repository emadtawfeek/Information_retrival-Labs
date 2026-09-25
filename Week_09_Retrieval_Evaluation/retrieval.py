import os
import re

STOP_WORDS = {
    "a", "an", "the", "is", "in", "for", "and", "are", "with",
    "like", "of", "to", "it", "be", "used", "uses", "that", "this",
    "was", "were", "by", "from", "on", "at", "or",
}
SAMPLE_DOCUMENTS = {
    "doc1": "Python is great for data science and machine learning",
    "doc2": "Java is used for enterprise applications and web development",
    "doc3": "Machine learning uses neural networks and decision trees",
    "doc4": "Python supports data analysis with libraries like Pandas",
    "doc5": "Java and C++ are used for game development and graphics",
}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_documents(folder_path):
    """Load UTF-8 .txt files; use five samples if missing or empty."""
    documents = {}
    if os.path.isdir(folder_path):
        for filename in sorted(os.listdir(folder_path)):
            filepath = os.path.join(folder_path, filename)
            if filename.endswith(".txt") and os.path.isfile(filepath):
                with open(filepath, "r", encoding="utf-8") as file:
                    documents[filename[:-4]] = file.read()
    if not documents:
        return SAMPLE_DOCUMENTS.copy()
    return documents


def tokenize(text):
    """Use the same ASCII-letter tokens as the supplied course files."""
    words = re.findall(r"[a-z]+", text.lower())
    return [word for word in words if word not in STOP_WORDS]

import math

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


def main():
    import sys
    documents = load_documents(os.path.join(BASE_DIR, "docs"))
    vocabulary, counts, df, idf, vectors = build_tfidf(documents)
    query = " ".join(sys.argv[1:]) or "python data analysis"
    print("Query:", query)
    vector = query_vector(query, vocabulary, idf)
    print("Query magnitude:", f"{magnitude(vector):.4f}")
    if magnitude(vector) == 0:
        print("No indexed query terms with nonzero weight.")
    print("Ranking:")
    for position, (name, score) in enumerate(
        rank_query(query, vocabulary, idf, vectors), 1
    ):
        print(f"{position:2}. {name:6} {score:.4f}")


if __name__ == "__main__":
    main()
