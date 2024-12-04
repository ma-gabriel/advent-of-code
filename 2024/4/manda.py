
def horizontal(lst, x, y, rev=False):
    if x > len(lst[y]) - 4 and not rev: return False
    if x < 3 and rev : return False

    if not rev and lst[y][x:x+4] == list("XMAS") : return True
    if rev and lst[y][x-3:x+1][::-1] == list("XMAS") : return True
    return False

def vertical(lst, x, y, rev=False):
    if y > len(lst) - 4 and not rev: return False
    if y < 3 and rev: return False

    if not rev and [l[x] for l in lst[y:y+4]] == list("XMAS"): return True
    if rev and [l[x] for l in lst[y-3:y+1][::-1]] == list("XMAS"): return True
    return False

def bottomright(lst, x, y, rev=False):
    if (y > len(lst) - 4 or x > len(lst[y]) - 4) and not rev : return False
    if (y < 3 or x < 3) and rev: return False

    if not rev and [l[x + i] for i, l in enumerate(lst[y:y+4])] == list("XMAS"): return True
    if rev and [l[x - i] for i, l in enumerate(lst[y-3:y+1][::-1])] == list("XMAS"): return True 
    return False

def bottomleft(lst, x, y, rev=False):
    if (y > len(lst) - 4 or x < 3) and not rev : return False
    if (y < 3 or x > len(lst[y]) - 4) and rev: return False

    if not rev and [l[x - i] for i, l in enumerate(lst[y:y+4])] == list("XMAS"): return True
    if rev and [l[x + i] for i, l in enumerate(lst[y-3:y+1][::-1])] == list("XMAS"): return True
    return False

if __name__ == "__main__":

    lst = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            lst.append(list(line.upper().replace('\n', '')))

    res = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            res += horizontal(lst, j, i)
            res += horizontal(lst, j, i, rev=True)
            res += vertical(lst, j, i)
            res += vertical(lst, j, i, rev=True)
            res += bottomright(lst, j, i)
            res += bottomright(lst, j, i, rev=True)
            res += bottomleft(lst, j, i)
            res += bottomleft(lst, j, i, rev=True)

    print(res)
