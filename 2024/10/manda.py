
def step(doc, i, j, ids):
    res = 0
    elem = doc[i][j][0]
    if elem == 9:
        if doc[i][j][2] == ids:
            return 0
        doc[i][j][2] = ids
        return 1
    doc[i][j][1] = '.'
    if doc[i - 1][j][0] == elem + 1 and doc[i - 1][j][1] == ' ':
        res += step(doc, i - 1, j, ids)
    if doc[i + 1][j][0] == elem + 1 and doc[i + 1][j][1] == ' ':
        res += step(doc, i + 1, j, ids)
    if doc[i][j - 1][0] == elem + 1 and doc[i][j - 1][1] == ' ':
        res += step(doc, i, j - 1, ids)
    if doc[i][j + 1][0] == elem + 1 and doc[i][j + 1][1] == ' ':
        res += step(doc, i, j + 1, ids)
    doc[i][j][1] = ' '
    return res

if __name__ == "__main__":
    order = dict()
    doc = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            line = list(map(lambda x: [0, ' ', None] if x == '0' else [int(x), ' ', None], line[:-1]))
            line = [[-1, ',']] + line + [[-1, ',']]
            doc.append(line)
    doc.insert(0, list([[-1,',']] * len(doc[0])))
    doc.append(list([[-1,',']] * len(doc[0])))

    res = 0
    ids = 0
    for i in range(len(doc)):
        for j in range(len(doc[i])):
            if doc[i][j] == [0, ' ', None]:
                res += step(doc, i, j, ids)
                ids += 1
    print(res)
