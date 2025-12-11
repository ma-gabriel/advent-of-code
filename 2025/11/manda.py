
def small_rec(init):
    if init == "out":
        return 1
    res = 0
    for to in data[init]:
        res += small_rec(to)
    return res


with open("entry.txt") as my_file:
    data = dict()
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        data[line[:3]] = tuple(line[4:].split())
    res = small_rec("you")

print(res)
