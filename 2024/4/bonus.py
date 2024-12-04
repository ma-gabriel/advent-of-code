
def bottomright(lst, x, y, rev=False):
    if (y > len(lst) - 3 or x > len(lst[y]) - 3) and not rev : return False
    if (y < 2 or x < 2) and rev: return False

    if not rev and [l[x + i] for i, l in enumerate(lst[y:y+3])] == list("MAS"): return True
    if rev and [l[x - i] for i, l in enumerate(lst[y-2:y+1][::-1])] == list("MAS"): return True 
    return False

def bottomleft(lst, x, y, rev=False):
    if (y > len(lst) - 3 or x < 2) and not rev : return False
    if (y < 2 or x > len(lst[y]) - 3) and rev: return False

    if not rev and [l[x - i] for i, l in enumerate(lst[y:y+3])] == list("MAS"): return True
    if rev and [l[x + i] for i, l in enumerate(lst[y-2:y+1][::-1])] == list("MAS"): return True
    return False

def xmas(lst, x, y):
    if lst[y][x] != 'A': return False
    if bottomright(lst, x-1, y-1) and bottomleft(lst, x+1, y-1): return True
    if bottomright(lst, x-1, y-1) and bottomleft(lst, x-1, y+1, rev=True): return True
    if bottomright(lst, x+1, y+1, rev=True) and bottomleft(lst, x+1, y-1): return True
    if bottomright(lst, x+1, y+1, rev=True) and bottomleft(lst, x-1, y+1, rev=True): return True
    return False

if __name__ == "__main__":

    lst = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            lst.append(list(line.upper().replace('\n', '')))

    res = 0
    for i in range(1, len(lst) - 1):
        for j in range(1, len(lst[i]) - 1):
            res += xmas(lst, j, i)

    print(res)
