
def find_player(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] in "^>v<":
                return j, i, lst[i][j]

def next_move(lst, x, y, d):
    if lst[y][x] == 'E':
        return None
    return x, y, d

def next_coo(lst, x, y, d):
    match lst[y][x]:
        case '^':
            if lst[y - 1][x] == '#':
                lst[y][x] = '>'
                d = '>'
                return next_coo(lst, x, y, d)
            y -= 1
        case 'v':
            if lst[y + 1][x] == '#':
                lst[y][x] = '<'
                d = '<'
                return next_coo(lst, x, y, d)
            y += 1
        case '>':
            if lst[y][x + 1] == '#':
                lst[y][x] = 'v'
                d = 'v'
                return next_coo(lst, x, y, d)
            x += 1
        case '<':
            if lst[y][x - 1] == '#':
                lst[y][x] = '^'
                d = '^'
                return next_coo(lst, x, y, d)
            x -= 1
    return x, y, d

if __name__ == "__main__":
    lst = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            line = ['E'] + list(line[:-1]) + ['E']
            lst.append(line)
    lst.insert(0, list('E' * len(lst[0])))
    lst.append(list('E' * len(lst[0])))
    coo = find_player(lst)
    while tmp:= next_move(lst, *next_coo(lst, *coo)):
        lst[coo[1]][coo[0]] = 'X'
        lst[tmp[1]][tmp[0]] = tmp[2]
        coo = tmp
    lst[coo[1]][coo[0]] = 'X'

    print(sum(row.count('X') for row in lst))
