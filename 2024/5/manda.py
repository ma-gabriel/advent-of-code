
def is_well_situated(order, page, i):
    if page[i] not in order:
        return True
    for elem in order[page[i]]:
        if elem in page[:i]:
            return False
    return True
    

def is_in_order(order, page):
    for i in range(len(page)):
        if not is_well_situated(order, page, i):
            return False
    return True

def valid(order, pages):
    res = 0
    for page in pages:
        if is_in_order(order, page):
            res += int(page[len(page) // 2])
    return (res)


if __name__ == "__main__":
    order = dict()
    pages = list()
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
    print(valid(order, pages))
