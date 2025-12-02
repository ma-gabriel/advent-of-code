
res = 0

with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if (len(line) == 0):
            continue
        if line[-1] == ',':
            line = line[:-1]
        for ranges in line.split(','):
            firstId, lastId = ranges.split('-')
            for Id in range(int(firstId), int(lastId) + 1):
                strId = str(Id)
                if strId[:len(strId) // 2] == strId[len(strId) // 2:]:
                    res += Id
print(res)
