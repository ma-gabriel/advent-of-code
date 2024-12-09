
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
    elem = i - 1
    while elem:
        space = res.count(elem)
        for i in range(min(res.index(elem),len(res) - space)):
            if res[i:i + space].count('.') == space:
                res = list(map(lambda x: '.' if x == elem else x, res))
                res = res[:i] + [elem] * space + res[i + space:]
                break
        elem -= 1
    total = 0
    for i, elem in enumerate(res):
        if elem != '.':
            total += i * elem
    print(total)
