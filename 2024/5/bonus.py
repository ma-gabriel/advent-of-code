
from manda import is_in_order
from manda import is_well_situated

if __name__ == "__main__":
    order = dict()
    pages = list()
    res = 0
    with open("entry.txt") as my_file:
        for line in my_file:
            line = line[:-1]
            if len(line) == 0: break
            tmp = line.split('|')
            if tmp[0] not in order: order[tmp[0]] = [tmp[1]]
            else: order[tmp[0]].append(tmp[1])
        for line in my_file:
            line = line[:-1]
            pages.append(list(line.split(',')))
    for page in pages:
        modified = False
        tmp = page
        while not is_in_order(order, tmp):
            modified = True
            for i in range(len(tmp)):
                if is_in_order(order, tmp):
                    break
                j = 0
                while not is_well_situated(order, tmp, i):
                    tmp.insert(j, tmp.pop(i))
                    j+= 1
        if not is_in_order(order, tmp):
            print("AAAAAAAH")
        if modified:
            res += int(tmp[len(tmp) // 2])
    print(res)
