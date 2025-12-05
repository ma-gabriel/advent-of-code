
res = 0
ids = []

with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            if len(ids): break
            else: continue
        ids.append([int(string) for string in line.split('-')])
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            break
        num = int(line)
        if any(id_range[0] <= num <= id_range[1] for id_range in ids):
            res += 1

print(res)
