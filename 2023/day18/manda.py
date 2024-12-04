file = open("valu.txt")


maps = [['.' for _ in range(500)] for _ in range(350)]

coo = [300, 100]
while (line := file.readline()):
    if line[0] == 'R':
        for _ in range(int(line[1:4])):
            maps[coo[0]][coo[1]] = '#'
            coo[1] += 1
    if line[0] == 'D':
        for _ in range(int(line[1:4])):
            maps[coo[0]][coo[1]] = '#'
            coo[0] += 1
    if line[0] == 'L':
        for _ in range(int(line[1:4])):
            maps[coo[0]][coo[1]] = '#'
            coo[1] -= 1
    if line[0] == 'U':
        for _ in range(int(line[1:4])):
            maps[coo[0]][coo[1]] = '#'
            coo[0] -= 1
file.close()

coo = [301, 101]
for j in range(len(maps)):
    inside = 0
    i = 0
    while i < len(maps[j]):
        if not inside and maps[j][i] == '#':
            bas = maps[j + 1][i]
            ex_i = i + 1
            while maps[j][i] == '#':
                i+= 1
            inside = maps[j + 1][i - 1] != bas or ex_i == i
        elif maps[j][i] == '#':
            bas = maps[j + 1][i]
            ex_i = i + 1
            while maps[j][i] == '#':
                i+= 1
            inside =not ( maps[j + 1][i - 1] != bas or ex_i == i)
        elif inside:
            maps[j][i] = '#'
            i += 1
        else:
            i+=1
res = 0
for i in maps:
    for j in i:
        if j == '#':
            res +=1
print(res)
