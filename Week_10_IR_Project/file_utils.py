"""Strict loader for the final project: no fallback collection."""
import os


def load_documents(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError("Create a docs folder containing UTF-8 .txt files")
    documents = {}
    for filename in sorted(os.listdir(folder_path)):
        path = os.path.join(folder_path, filename)
        if filename.endswith(".txt") and os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                documents[filename[:-4]] = file.read()
    if not documents:
        raise ValueError("The docs folder contains no .txt documents")
    return documents
