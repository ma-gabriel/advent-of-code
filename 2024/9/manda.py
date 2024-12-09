
if __name__ == "__main__":

    infile = str()
    res = list();
    with open("entry.txt") as my_file:
        for line in my_file:
            infile += line[:-1]
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
    while '.' in res:
        res[res.index('.')] = res[-1]
        res.pop(-1)
    total = 0
    for j, elem in enumerate(res):
        total += j * elem
    print(total)
