
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
    res_ids = []
    for id_range in ids:
        for id_range2 in ids:
            if id_range == id_range2:
                continue
            if id_range2[0] <= id_range[0] <= id_range2[1]:
                id_range[0] = id_range2[1] + 1
            elif id_range2[0] <= id_range[1] <= id_range2[1]:
                id_range[1] = id_range2[0] - 1
        if (id_range[0] <= id_range[1]):
            res_ids.append(tuple(id_range))
res_ids = set(res_ids)
print(sum([id_range[1] - id_range[0] + 1 for id_range in res_ids]))
