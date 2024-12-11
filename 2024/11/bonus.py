

def update(stones):
    res = list()
    for stone, poids in stones:
        strStone = str(stone)
        lenStone = len(strStone)
        if stone == 0:
            res.append([1, poids])
        elif not lenStone % 2:
            res.append([int(strStone[:lenStone // 2]), poids])
            res.append([int(strStone[lenStone // 2:]), poids])
        else:
            res.append([stone * 2024, poids])
    dictio = dict()
    for stone, poids in res:
        if stone not in dictio:
            dictio[stone] = poids
        else:
            dictio[stone] += poids
    return list(dictio.items())

if __name__ == "__main__":

    infile = str()
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile += line[:-1]
            else:
                infile += line
    stones = [[int(elem), 1] for elem in infile.split()]
    for i in range(75):
        stones = update(stones)
    print(sum(dict(stones).values()))
