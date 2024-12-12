
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
    for i in range(len(doc)):
        for j in range(len(doc[i])):
            if doc[i][j] == True:
                doc[i][j] = False

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
def count_side(doc, i, j):
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

if __name__ == "__main__":

    infile = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile.append([None] + list(line[:-1]) + [None])
            else:
                infile.append([None] + list(line) + [None])
    infile.insert(0, list([None] * len(infile[0])))
    infile.append(list([None] * len(infile[0])))
    total = 0
    for i, line in enumerate(infile):
        for j, elem in enumerate(line):
            if infile[i][j]:
                total += rec(infile, i, j, elem) * count_side(infile, i, j)
                falsing(infile)
    print(total)
