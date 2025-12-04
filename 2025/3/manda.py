
res = 0

with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if (len(line) == 0):
            continue
        tmp = max(line[:-1])
        res += int(tmp) * 10 + int(max(line[line.find(tmp) + 1:]))

print(res)
