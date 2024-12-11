def is_valid(doc, i, j):
    if i < 0 or j < 0:
        return 0
    if i >= len(doc):
        return 0
    if j >= len(doc[i]):
        return 0
    return 1

def change(doc, i, j, elem, tmp):
    if (i, j) in tmp[elem]:
        return 0
    tmp[elem].append((i, j))
    return 1

total = 0
with open("entry.txt") as my_file:
    doc = list()
    for line in my_file:
        doc.append(list(line)[:-1])

antennas = dict()
for i in range(len(doc)):
    for j in range(len(doc[i])):
        elem = doc[i][j]
        if elem == '.':
            continue
        if elem in antennas:
            antennas[elem].append((i, j))
        else:
            antennas[elem] = [(i, j)]

sub = dict()
for elem, lst in antennas.items():
    sub[elem] = list()
    for coo1 in lst:
        for coo2 in lst:
            if coo1 == coo2:
                continue
            d1, d2 = coo1[0] - coo2[0], coo1[1] - coo2[1]
            if is_valid(doc, coo1[0] + d1, coo1[1] + d2):
                change(doc, coo1[0] + d1, coo1[1] + d2, elem, sub)
            if is_valid(doc, coo2[0] - d1, coo2[1] - d2):
                change(doc, coo2[0] - d1, coo2[1] - d2, elem, sub)
res = set()
for value in sub.values():
    for val in value:
        res.add(val)
print(len(res))
