
def step(doc, i, j):
    res = 0
    elem = doc[i][j]
    if elem == 9:
        return 1
    if doc[i - 1][j] == elem + 1:
        res += step(doc, i - 1, j)
    if doc[i + 1][j] == elem + 1:
        res += step(doc, i + 1, j)
    if doc[i][j - 1] == elem + 1:
        res += step(doc, i, j - 1)
    if doc[i][j + 1] == elem + 1:
        res += step(doc, i, j + 1)
    return res

if __name__ == "__main__":
    order = dict()
    doc = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            line = [-1] + [int(c) for c in line[:-1]] + [-1]
            doc.append(line)
    doc.insert(0, list([-1] * len(doc[0])))
    doc.append(list([-1] * len(doc[0])))

    res = 0
    for i in range(len(doc)):
        for j in range(len(doc[i])):
            if doc[i][j] == 0:
                res += step(doc, i, j)
    print(res)
