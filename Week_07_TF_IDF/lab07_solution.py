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


def main():
    documents = load_documents(os.path.join(BASE_DIR, "docs"))
    vocabulary, counts, df, idf, vectors = build_tfidf(documents)
    names = sorted(documents)
    print("Documents:", names)
    print("Term         DF     IDF    TF in doc9")
    for term in ["python", "data", "retrieval"]:
        print(f"{term:12} {df.get(term, 0):2} {idf.get(term, 0):8.4f}",
              counts.get("doc9", {}).get(term, 0))
    # Five columns per block keep the full matrix readable on paper.
    for start in range(0, len(names), 5):
        block = names[start:start + 5]
        print("\nTF-IDF matrix:", " ".join(block))
        for i, term in enumerate(vocabulary):
            values = " ".join(f"{vectors[name][i]:7.3f}" for name in block)
            print(f"{term:12} {values}")


if __name__ == "__main__":
    main()
