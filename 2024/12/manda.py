
def rec(infile, i, j, elem):
    area, perimeter = 1, 4
    infile[i][j] = True
    if i > 0:
        if (infile[i - 1][j] == True):
            perimeter -= 1
        elif (infile[i - 1][j] == elem):
            tmp = rec(infile, i - 1, j, elem)
            perimeter += tmp[1] - 1
            area += tmp[0]
    if j > 0:
        if (infile[i][j - 1] == True):
            perimeter -= 1
        elif (infile[i][j - 1] == elem):
            tmp = rec(infile, i, j - 1, elem)
            perimeter += tmp[1] - 1
            area += tmp[0]
    if i < len(infile) - 1:
        if (infile[i + 1][j] == True):
            perimeter -= 1
        elif (infile[i + 1][j] == elem):
            tmp = rec(infile, i + 1, j, elem)
            perimeter += tmp[1] - 1
            area += tmp[0]
    if j < len(infile[i]) - 1:
        if (infile[i][j + 1] == True):
            perimeter -= 1
        elif (infile[i][j + 1] == elem):
            tmp = rec(infile, i, j + 1, elem)
            perimeter += tmp[1] - 1
            area += tmp[0]
    return area, perimeter

def falsing(doc):
    for i in range(len(doc)):
        for j in range(len(doc[i])):
            if doc[i][j] == True:
                doc[i][j] = False

if __name__ == "__main__":

    infile = list()
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile.append(list(line[:-1]))
            else:
                infile.append(list(line))
    total = 0
    for i, line in enumerate(infile):
        for j, elem in enumerate(line):
            if infile[i][j]:
                tmp = rec(infile, i, j, elem)
                total += tmp[0] * tmp[1]
                falsing(infile)
    print(total)
            
            
