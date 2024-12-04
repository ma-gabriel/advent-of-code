
file = open("valu.txt")

maps = list()
while (line := file.readline()):
    maps.append(list(line))

res = [[ 1000000000 for _ in range(len(maps))] for _ in range(len(maps[0]))]
