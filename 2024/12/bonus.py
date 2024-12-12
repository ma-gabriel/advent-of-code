import sys

sys.setrecursionlimit(100000000)

def rec(infile, i, j, elem):
    area = 1
    infile[i][j] = True
    if i > 0 and infile[i - 1][j] == elem:
           area += rec(infile, i - 1, j, elem)
    if j > 0 and infile[i][j - 1] == elem:
            area += rec(infile, i, j - 1, elem)
    if i < len(infile) - 1 and infile[i + 1][j] == elem:
            area += rec(infile, i + 1, j, elem)
    if j < len(infile[i]) - 1 and infile[i][j + 1] == elem:
            area += rec(infile, i, j + 1, elem)
    return area

def falsing(doc):
    for i in range(1, len(doc) - 1):
        for j in range(1, len(doc[i]) - 1):
            if doc[i][j] == True:
                doc[i][j] = 'FALSE'

def go_down(doc, i, j):
    if doc[i + 1][j] == True: i += 1
    while doc[i][j - 1] != True and doc[i + 1][j] == True: i += 1
    if doc[i][j - 1] == True:
        return i, j, 3
    return i, j, 2

def go_left(doc, i, j):
    if doc[i][j - 1] == True: j -= 1
    while doc[i - 1][j] != True and doc[i][j - 1] == True: j -= 1
    if doc[i - 1][j] == True:
        return i, j, 1
    return i, j, 0

def go_up(doc, i, j):
    if doc[i - 1][j] == True: i -= 1
    while doc[i][j + 1] != True and doc[i - 1][j] == True: i -= 1
    if doc[i][j + 1] == True:
        return i, j, 2
    return i, j, 3

def go_right(doc, i, j):
    if doc[i][j + 1] == True: j += 1
    while doc[i + 1][j] != True and doc[i][j + 1] == True: j += 1
    if doc[i + 1][j] == True:
        return i, j, 0
    return i, j, 1

'''
we go clockwise
i++ -> d = 0
i-- -> d = 1
j++ -> d = 2
j-- -> d = 3
'''
def count_side_exterior(doc, i, j):
    d = 0
    sides = 0
    first = True
    start = None
    while start != (i, j, d) or sides < 4:
        sides += 1
        if d == 0:
            i, j, d = go_down(doc, i, j)
        elif d == 3:
            i, j, d = go_left(doc, i, j)
        elif d == 1:
            i, j, d = go_up(doc, i, j)
        elif d == 2:
            i, j, d = go_right(doc, i, j)
        if first:
            start = (i, j, d)
            first = False
    return sides - 1

def propa(doc, i, j, prof=0):
    res = None
    d = ((-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1))
    doc[i][j] = doc[i][j].lower()
    if doc[i][j + 1] is True:
        res = i, j + 1
    if not any([doc[i + d1][j + d2] == True for d1, d2 in d]):
        return
    for d1, d2 in d:
        if doc[i + d1][j + d2] not in [True, None] and doc[i + d1][j + d2].isupper():
            if not res:
                res = propa(doc, i + d1, j + d2, prof=prof + 1)
            else:
                propa(doc, i + d1, j + d2, prof=prof + 1)
    return res

def find_interior(doc):
    coos = list()
    for i in range(2, len(doc) - 2):
        for j in range(1, len(doc[i]) -1):
            if doc[i][j] not in [True, None] and doc[i][j].isupper():
                tmp = propa(doc, i, j)
                if tmp: coos.append(tmp)
    for i in range(1, len(doc) - 1):
        for j in range(1, len(doc[i]) -1):
            if doc[i][j] != True:
                doc[i][j] = doc[i][j].upper()
    return coos

def count_side(doc, i, j):
    res = 0
    coos = find_interior(doc)
    for coo in coos:
        res += count_side_exterior(doc, *coo)
    return res

if __name__ == "__main__":
    infile = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile.append([None, 'FALSE'] + list(line[:-1]) + [None])
            else:
                infile.append([None, 'FALSE'] + list(line) + [None])
    infile.insert(0, list([None] * len(infile[0])))
    infile.append(list([None] * len(infile[0])))
    total = 0
    for i, line in enumerate(infile):
        for j, elem in enumerate(line):
            if infile[i][j] not in ['FALSE', None]:
                total += rec(infile, i, j, elem) * count_side(infile, i, j)
                print(f"getting the price for the crop {elem}")
                falsing(infile)
    print(total)
