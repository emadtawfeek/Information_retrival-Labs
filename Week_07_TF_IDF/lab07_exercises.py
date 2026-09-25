"""Week 7: student starter. Finish TODOs before checking results."""
import os
import re
import math

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STOP_WORDS = {"a", "an", "the", "is", "and", "for", "with"}


def tfidf_weight(term, tokens, document_frequency, total):
    # TODO: Use raw TF and math.log(total / DF).
    return None


def main():
    print("Starter only: TODO functions are not completed yet.")
    print(tfidf_weight("data", ["data", "data"], 2, 3))


if __name__ == "__main__":
    main()
