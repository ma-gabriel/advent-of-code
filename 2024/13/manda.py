
def get_score(infile):
    res = 401;
    A_pressed = [0, 0, 0]
    for _ in range(100):
        B_pressed = [0, 0, 0]
        for _ in range(100):
            if A_pressed[0] + B_pressed[0] == infile['P'][0] and A_pressed[1] + B_pressed[1] == infile['P'][1] and A_pressed[2] * 3 + B_pressed[2] <= res:
                res = A_pressed[2] * 3 + B_pressed[2]
            B_pressed[0] += infile['B'][0]
            B_pressed[1] += infile['B'][1]
            B_pressed[2] += 1
        A_pressed[0] += infile['A'][0]
        A_pressed[1] += infile['A'][1]
        A_pressed[2] += 1
    return res


if __name__ == "__main__":
    infile = dict()
    total = 0
    with open("entry.txt") as my_file:
        for line in my_file:
            if line.startswith("Button A:"):
                infile['A'] = (int(line[12:14]), int(line[18:20]))
            elif line.startswith("Button B:"):
                infile['B'] = (int(line[12:14]), int(line[18:20]))
            elif line.startswith("Prize:"):
                infile['P'] = (int(line[line.find("X=") + 2: line.find(",")]), int(line[line.find("Y=") + 2:]))
            if line == "\n":
                tmp = get_score(infile)
                if tmp != 401: total += tmp
    print(total)



