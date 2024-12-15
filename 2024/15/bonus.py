
def valid_down(doc, i, j):
    match doc[i + 1][j]:
        case '.':
            return True
        case '#':
            return False
        case '[':
            return valid_down(doc, i + 1, j) and valid_down(doc, i + 1, j + 1)
        case ']':
            return valid_down(doc, i + 1, j - 1) and valid_down(doc, i + 1, j)

def push_down(doc, i, j):
    match doc[i + 1][j]:
        case '[':
            push_down(doc, i + 1, j)
            push_down(doc, i + 1, j + 1)
        case ']':
            push_down(doc, i + 1, j - 1)
            push_down(doc, i + 1, j)
    doc[i + 1][j] = doc[i][j]
    doc[i][j] = '.'

def valid_up(doc, i, j):
    match doc[i - 1][j]:
        case '.':
            return True
        case '#':
            return False
        case '[':
            return valid_up(doc, i - 1, j) and valid_up(doc, i - 1, j + 1)
        case ']':
            return valid_up(doc, i - 1, j - 1) and valid_up(doc, i - 1, j)

def push_up(doc, i, j):
    match doc[i - 1][j]:
        case '[':
            push_up(doc, i - 1, j)
            push_up(doc, i - 1, j + 1)
        case ']':
            push_up(doc, i - 1, j - 1)
            push_up(doc, i - 1, j)
    doc[i - 1][j] = doc[i][j]
    doc[i][j] = '.'

def Do(doc, move, i, j):
    if move not in "<v>^":
        return i, j
    d = 1
    match move:
        case 'v':
            if not valid_down(doc, i, j): return i, j
            push_down(doc, i, j)
            return i + 1, j
        case '^':
            if not valid_up(doc, i, j): return i, j
            push_up(doc, i, j)
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

def upgrade(doc):
    tmp = list()
    for line in doc:
        tmp.append(list())
        for elem in line:
            if elem == '.':
                tmp[-1] += ['.', '.']
            elif elem == '#':
                tmp[-1] += ['#', '#']
            elif elem == 'O':
                tmp[-1] += ['[', ']']
            else:
                tmp[-1] += ['@', '.']
    return tmp

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
    doc = upgrade(doc)
    coos = find(doc)
    if not coos:
        print(r"player not found, entry either don't contain map, or contain the \n wait too soon")
        exit(1)
    for move in moves:
        coos = Do(doc, move, *coos)
    res = 0
    for i, line in enumerate(doc):
        for j, elem in enumerate(line):
            if elem == '[': res += 100 * i + j
    print(res)
