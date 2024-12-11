

def update(stones):
    if stone == 0:
        return [1]
    strStone = str(stone)
    lenStone = len(strStone)
    if lenStone % 2:
        return [stone * 2024]
    return [int(strStone[:lenStone // 2]), int(strStone[lenStone // 2:])]

if __name__ == "__main__":

    infile = str()
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile += line[:-1]
            else:
                infile += line
    stones = [int(elem) for elem in infile.split()]
    for i in range(75):
        tmp = list()
        for stone in stones:
            tmp += update(stone)
        stones = tmp
        print(f"blink {i + 1} out of 75")

    print(len(stones))
