import json
import os
from retrieval import load_documents, build_tfidf, rank_query

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def precision(retrieved, relevant):
    retrieved = set(retrieved)
    relevant = set(relevant)
    if not retrieved:
        return 0.0
    return len(retrieved & relevant) / len(retrieved)


def recall(retrieved, relevant):
    relevant = set(relevant)
    if not relevant:
        return 0.0
    return len(set(retrieved) & relevant) / len(relevant)


def f1_score(p, r):
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)


def unique_ranking(ranked_docs):
    result = []
    for name in ranked_docs:
        if name not in result:
            result.append(name)
    return result


def precision_at_k(ranked_docs, relevant_docs, k):
    if k <= 0:
        raise ValueError("k must be positive")
    top = unique_ranking(ranked_docs)[:k]
    # Unfilled positions count as nonrelevant: denominator stays k.
    return len(set(top) & set(relevant_docs)) / k


def recall_at_k(ranked_docs, relevant_docs, k):
    if k <= 0:
        raise ValueError("k must be positive")
    return recall(unique_ranking(ranked_docs)[:k], relevant_docs)


def report(label, ranked_docs, relevant, k=3):
    top = unique_ranking(ranked_docs)[:k]
    true_positive = len(set(top) & set(relevant))
    false_positive = len(set(top) - set(relevant))
    false_negative = len(set(relevant) - set(top))
    p = precision(top, relevant)
    r = recall(top, relevant)
    print(label, "top:", top)
    print("TP, FP, FN:", true_positive, false_positive, false_negative)
    print(f"Precision={p:.4f} Recall={r:.4f} F1={f1_score(p, r):.4f}")
    print(f"P@{k}={precision_at_k(ranked_docs, relevant, k):.4f}")
    print(f"R@{k}={recall_at_k(ranked_docs, relevant, k):.4f}")


def main():
    documents = load_documents(os.path.join(BASE_DIR, "docs"))
    vocabulary, counts, df, idf, vectors = build_tfidf(documents)
    path = os.path.join(BASE_DIR, "data", "relevance.json")
    with open(path, "r", encoding="utf-8") as file:
        judgments = json.load(file)
    for case in judgments:
        query = case["query"]
        relevant = set(case["relevant"])
        results = rank_query(query, vocabulary, idf, vectors)
        ranked = [name for name, score in results if score > 0]
        baseline = sorted(documents)  # Filename order, not relevance.
        print("\nQuery:", query)
        print("Relevant:", sorted(relevant))
        report("TF-IDF", ranked, relevant)
        report("Filename baseline", baseline, relevant)


if __name__ == "__main__":
    main()
