def is_valid(doc, i, j):
    if i < 0 or j < 0:
        return 0
    if i >= len(doc):
        return 0
    if j >= len(doc[j]):
        return 0
    return 1

total = 0
with open("entry.txt") as my_file:
    doc = list()
    for line in my_file:
        doc.append(list(line)[:-1])

    antennas = dict()
    for i in range(len(coo)):
        for j in range(len(coo[i])):
            elem = coo[i][j]
            if elem == '.':
                continue
            if elem in antennas:
                antennas[elem].append((i, j))
            else:
                antennas[elem] = [(i, j)]
    for elem, lst in antennas:
        for antenna1 in lst:
            for antenna2 in lst:
                if antenna1 == antenna2:
                    continue
                if is_valid(doc, antenna2[0]
    

print(total)
