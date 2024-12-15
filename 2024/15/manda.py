
def Do(doc, move, i, j):
    if move not in "<v>^":
        return i, j
    d = 1
    match move:
        case 'v':
            while doc[i + d][j] not in '.#': d += 1
            if doc[i + d][j] == '#': return i, j
            while d: doc[i + d][j] = doc[i + d - 1][j] ; d -= 1
            doc[i][j] = '.'
            return i + 1, j
        case '^':
            while doc[i - d][j] not in '.#': d += 1
            if doc[i - d][j] == '#': return i, j
            while d: doc[i - d][j] = doc[i - d + 1][j] ; d -= 1
            doc[i][j] = '.'
            return i - 1, j
        case '>':
            while doc[i][j + d] not in '.#': d += 1
            if doc[i][j + d] == '#': return i, j
            while d: doc[i][j + d] = doc[i][j + d - 1] ; d -= 1
            doc[i][j] = '.'
            return i, j + 1
        case '<':
            while doc[i][j - d] not in '.#': d += 1
            if doc[i][j - d] == '#': return i, j
            while d: doc[i][j - d] = doc[i][j - d + 1] ; d -= 1
            doc[i][j] = '.'
            return i, j - 1

def find(doc):
    for i, line in enumerate(doc):
        if '@' in line: return i, line.index('@')

if __name__ == "__main__":
    doc = list()
    moves = "";
    with open("entry.txt") as my_file:
        start = True
        for line in my_file:
            if line == "\n":
                start = False
            if start == True:
                doc.append(list(line[:-1]))
            else:
                moves += line
    coos = find(doc)
    if not coos:
        print(r"player not found, entry either don't contain map, or contain the \n wait too soon")
        exit(1)
    for move in moves:
        coos = Do(doc, move, *coos)
    res = 0
    for i, line in enumerate(doc):
        for j, elem in enumerate(line):
            if elem == 'O': res += 100 * i + j
    print(res)
