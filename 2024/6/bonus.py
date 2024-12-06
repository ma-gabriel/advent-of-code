
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
    import copy
    base = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            line = ['E'] + list(line[:-1]) + ['E']
            base.append(line)
    base.insert(0, list('E' * len(base[0])))
    base.append(list('E' * len(base[0])))
    coo_base = find_player(base)
    res = 0
    for i in range(1, len(base) - 1):
        print(f"{i = } out of {len(base) - 1}")
        for j in range(1, len(base[0]) - 1):
            if base[i][j] in "<>v^":
                break
            lst = copy.deepcopy(base)
            lst[i][j] = '#'
            coo = copy.deepcopy(coo_base)
            tracé = list() 
            tmp = find_player(lst)
            while (tmp := next_move(lst, *next_coo(lst, *coo))) and tmp  not in tracé:
                lst[coo[1]][coo[0]] = 'X'
                lst[tmp[1]][tmp[0]] = tmp[2]
                coo = tmp
                tracé.append(coo)
            if tmp in tracé:
                res += 1

    print(res)
