

if __name__ == "__main__":
    from manda import *
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

    coo = find_player(base)
    stamp = coo
    while tmp:= next_move(base, *next_coo(base, *coo)):
        base[coo[1]][coo[0]] = 'o'
        base[tmp[1]][tmp[0]] = tmp[2]
        coo = tmp
    base[coo[1]][coo[0]] = 'o'
    base[stamp[1]][stamp[0]] = stamp[2]
    for i in range(1, len(base) - 1):
        print(f"{i = } out of {len(base) - 2}")
        for j in range(1, len(base[0]) - 1):
            if base[i][j] != 'o':
                continue
            lst = copy.deepcopy(base)
            lst[i][j] = '#'
            coo = copy.deepcopy(coo_base)
            count = 0
            tmp = find_player(lst)
            while (tmp := next_move(lst, *next_coo(lst, *coo))) and count < 8000:
                lst[coo[1]][coo[0]] = 'X'
                lst[tmp[1]][tmp[0]] = tmp[2]
                coo = tmp
                count += 1
            if count == 8000: 
                res += 1

    print(res)
