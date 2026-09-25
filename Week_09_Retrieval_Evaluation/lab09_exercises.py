"""Week 9: student starter. Finish TODOs before checking results."""
import os
import re
import math

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STOP_WORDS = {"a", "an", "the", "is", "and", "for", "with"}


def precision_at_k(ranked_docs, relevant_docs, k):
    # TODO: Use unique document IDs and divide the relevant count by k.
    return None


def main():
    print("Starter only: TODO functions are not completed yet.")
    print(precision_at_k(["d1", "d2"], {"d2"}, 3))


if __name__ == "__main__":
    main()
