
res = 0

with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if (len(line) == 0):
            continue
        tmp = max(line[:-11])
        res += int(tmp) * 10 ** 11
        line = line[line.find(tmp) + 1:]
        for i in range(10, -1, -1):
            if (i):
                tmp = max(line[:-i])
            else:
                tmp = max(line)
            line = line[line.find(tmp) + 1:]
            res += int(tmp) * 10 ** i
print(res)
