
def check(infile, A, B):
    if infile['A'][0] * A + infile['B'][0] * B == infile['P'][0] and infile['A'][1] * A + infile['B'][1] * B == infile['P'][1]:
        return True
    return False

"""
infile['A'][0]   infile['B'][0]
infile['A'][1]   infile['B'][1]
"""
def get_score(infile):
    det = infile['A'][0] * infile['B'][1] - infile['A'][1] * infile['B'][0]
    if det == 0:
        return 0
    inverted = (infile['B'][1] / det, -1 * infile['B'][0] / det, -1 * infile['A'][1] / det,  infile['A'][0] / det)
    res = (int(round(inverted[0] * infile['P'][0] + inverted[1] * infile['P'][1])), int(round(inverted[2] * infile['P'][0] + inverted[3] * infile['P'][1])))
    if res[0] >= 0 and res[1] >= 0 and check(infile, res[0], res[1]):
        return res[0] * 3 + res[1]
    return 0


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
                infile['P'] = (10000000000000 + int(line[line.find("X=") + 2: line.find(",")]), 10000000000000 + int(line[line.find("Y=") + 2:]))
            if line == "\n":
                tmp = get_score(infile)
                print("new machine", tmp)
                total += tmp
    print(total)
