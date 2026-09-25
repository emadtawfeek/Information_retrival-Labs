"""Week 1: create and load a small UTF-8 document collection."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_documents(folder_path):
    documents = {}
    for filename in sorted(os.listdir(folder_path)):
        path = os.path.join(folder_path, filename)
        if filename.endswith(".txt") and os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                documents[filename[:-4]] = file.read()
    return documents


def main():
    folder = os.path.join(BASE_DIR, "docs")
    if not os.path.exists(folder):
        os.makedirs(folder)
    samples = {
        "doc1": "Python supports data analysis.\n",
        "doc2": "Java supports web development.\n",
        "doc3": "Networks connect computers.\n",
    }
    for name, text in samples.items():
        path = os.path.join(folder, name + ".txt")
        if not os.path.exists(path):  # Preserve student edits on reruns.
            with open(path, "w", encoding="utf-8") as file:
                file.write(text)
    # This disposable demonstration file is reset on each run.
    notes_path = os.path.join(BASE_DIR, "data", "notes.txt")
    with open(notes_path, "w", encoding="utf-8") as file:
        file.write("First line\n")
    with open(notes_path, "a", encoding="utf-8") as file:
        file.write("Appended line\n")
    with open(notes_path, "r", encoding="utf-8") as file:
        print("readline:", repr(file.readline()))
        print("remaining readlines:", file.readlines())
    with open(notes_path, "r", encoding="utf-8") as file:
        print("read:", repr(file.read()))
    for name, text in load_documents(folder).items():
        print(name, "->", text.strip())


if __name__ == "__main__":
    main()
