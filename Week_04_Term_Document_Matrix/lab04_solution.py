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

def build_matrix(documents):
    doc_names = sorted(documents)
    words_in_docs = {}
    all_words = []
    for name in doc_names:
        words_in_docs[name] = tokenize(documents[name])
        all_words.extend(words_in_docs[name])
    matrix = {}
    for term in sorted(set(all_words)):
        row = []
        for name in doc_names:
            row.append(1 if term in words_in_docs[name] else 0)
        matrix[term] = row
    return matrix, doc_names


def print_matrix(matrix, doc_names):
    print("Term".ljust(14), "|", " | ".join(doc_names))
    for term, row in matrix.items():
        values = " | ".join(str(bit).center(4) for bit in row)
        print(term.ljust(14), "|", values)


def main():
    documents = load_documents(os.path.join(BASE_DIR, "docs"))
    matrix, doc_names = build_matrix(documents)
    print_matrix(matrix, doc_names)


if __name__ == "__main__":
    main()
