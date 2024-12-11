

def update(stones):
    res = list()
    for stone in stones:
        strStone = str(stone)
        lenStone = len(strStone)
        if stone == 0:
            res.append(1)
        elif not lenStone % 2:
            res.append(int(strStone[:lenStone // 2]))
            res.append(int(strStone[lenStone // 2:]))
        else:
            res.append(stone * 2024)
    return res

if __name__ == "__main__":

    infile = str()
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile += line[:-1]
            else:
                infile += line
    stones = [int(elem) for elem in infile.split()]
    for i in range(25):
        stones = update(stones)
    print(len(stones))
