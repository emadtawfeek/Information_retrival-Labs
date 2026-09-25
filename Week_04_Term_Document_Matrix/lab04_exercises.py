"""Week 4: student starter. Finish TODOs before checking results."""
import os
import re
import math

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STOP_WORDS = {"a", "an", "the", "is", "and", "for", "with"}


def build_matrix(documents):
    # TODO: Return a term-to-bits dictionary and sorted document IDs.
    return {}, sorted(documents)


def main():
    print("Starter only: TODO functions are not completed yet.")
    print(build_matrix({"d1": "python data", "d2": "java"}))


if __name__ == "__main__":
    main()
