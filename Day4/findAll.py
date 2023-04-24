def findAll(word, substring):
    indices = []
    start = 0
    while True:
        index = word.find(substring, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices

