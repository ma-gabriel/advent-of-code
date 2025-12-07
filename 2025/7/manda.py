
res = 0
last = None
with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = list(line[:-1])
        if len(line) == 0:
            continue
        for i, elem in enumerate(line):
            if elem == '.' and last and last[i] in ['|', 'S']:
                line[i] = '|'
            if elem == '^' and last and last[i] in ['|']:
                res += 1
                line[i - 1] = line[i + 1] = '|'
        last = line
print(res)
