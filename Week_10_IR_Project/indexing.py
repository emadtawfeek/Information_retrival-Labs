from preprocessing import tokenize

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
