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

def parse_query(query):
    """Grammar: [NOT] term (AND [NOT] term)*; no OR or parentheses."""
    clauses = re.split(r"\bAND\b", query.strip(), flags=re.IGNORECASE)
    parsed = []
    for clause in clauses:
        match = re.fullmatch(
            r"(NOT\s+)?([a-z]+)", clause.strip(), re.IGNORECASE
        )
        if match is None:
            raise ValueError("Use: term AND term AND NOT term")
        term = match.group(2).lower()
        if term in {"and", "not", "or"}:
            raise ValueError("An operator cannot be used as a term")
        parsed.append((match.group(1) is not None, term))
    return parsed

def build_index(documents):
    index = {}
    for name, text in documents.items():
        for word in tokenize(text):
            if word not in index:
                index[word] = set()
            index[word].add(name)  # A document occurs at most once.
    for word in index:
        index[word] = sorted(index[word])
    return index


def intersect(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result


def negate(result_docs, all_docs):
    return [name for name in all_docs if name not in result_docs]


def run_query(query, index, all_docs, trace=True):
    result = None
    for negative, term in parse_query(query):
        current = index.get(term, [])
        if trace:
            print(term, "->", current)
        if negative:
            current = negate(current, all_docs)
            if trace:
                print("NOT", term, "->", current)
        if result is None:
            result = current
        else:
            result = intersect(result, current)
    return result

def main():
    import sys
    documents = load_documents(os.path.join(BASE_DIR, "docs"))
    index = build_index(documents)
    all_docs = sorted(documents)
    print("Loaded", len(documents), "documents")
    for term in ["python", "machine", "java"]:
        print(term, "->", index.get(term, []))
    if "--interactive" in sys.argv:
        print("Use term AND term AND NOT term; quit exits.")
        while True:
            try:
                query = input("Query > ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if query.lower() == "quit":
                break
            try:
                print("Matched docs:", run_query(query, index, all_docs))
            except ValueError as error:
                print(error)
    else:
        for query in ['python AND data', 'machine AND learning', 'python AND NOT java']:
            print("\nQuery:", query)
            print("Matched docs:", run_query(query, index, all_docs))


if __name__ == "__main__":
    main()
