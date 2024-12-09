
if __name__ == "__main__":

    infile = str()
    res = list();
    with open("entry.txt") as my_file:
        for line in my_file:
            if line[-1] == '\n':
                infile += line[:-1]
            else:
                infile += line
    space = False
    i = 0
    for char in infile:
        if space:
            res += ['.'] * int(char)
            space = False
        else:
            res += [i] * int(char)
            space = True
            i += 1
    print("created the \"00...111...2...333.44.5555.6666.777.888899\" text")
    while '.' in res:
        res[res.index('.')] = res[-1]
        res.pop(-1)
    print("ordered the files")
    total = 0
    for j, elem in enumerate(res):
        total += j * elem
    print(total)
