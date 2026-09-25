"""Run a demo, pass a query, or use --interactive for repeated search."""
import json
import os
import sys
from file_utils import load_documents
from preprocessing import tokenize
from indexing import build_index
from tfidf import build_tfidf
from ranking import rank_query
from evaluation import report

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def show_results(query, model, documents, judgments):
    vocabulary, counts, df, idf, vectors = model
    results = rank_query(query, vocabulary, idf, vectors)
    ranked = [name for name, score in results if score > 0]
    print("\nQuery:", query)
    print("Query tokens:", tokenize(query))
    if not ranked:
        print("No matching documents with a positive score.")
    for position, (name, score) in enumerate(results[:5], 1):
        if score > 0:
            print(f"{position}. {name} {score:.4f}")
            print("  ", documents[name].strip()[:90])
    # Judgments refer to exact query strings, ignoring case/whitespace.
    key = " ".join(query.lower().split())
    for case in judgments:
        if key == " ".join(case["query"].lower().split()):
            report("Evaluation", ranked, case["relevant"], k=3)
            return
    print("No predefined relevance judgments for this query.")


def main():
    try:
        documents = load_documents(os.path.join(BASE_DIR, "docs"))
    except (OSError, ValueError) as error:
        print("Collection error:", error)
        return
    index = build_index(documents)
    model = build_tfidf(documents)
    judgments_path = os.path.join(BASE_DIR, "data", "relevance.json")
    judgments = []
    if os.path.isfile(judgments_path):
        with open(judgments_path, "r", encoding="utf-8") as file:
            judgments = json.load(file)
        for case in judgments:
            unknown = set(case["relevant"]) - set(documents)
            if unknown:
                print("Judgments reference missing documents:", sorted(unknown))
                return
    print("Documents:", len(documents), "Vocabulary:", len(index))
    if "--interactive" in sys.argv:
        print("Enter a free-text query; quit exits.")
        while True:
            try:
                query = input("Search > ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if query.lower() == "quit":
                break
            if query:
                show_results(query, model, documents, judgments)
    else:
        query = " ".join(sys.argv[1:]) or "python data analysis"
        show_results(query, model, documents, judgments)


if __name__ == "__main__":
    main()
