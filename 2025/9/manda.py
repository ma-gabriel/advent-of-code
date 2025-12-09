
with open("entry.txt") as my_file:
    tiles = []
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        tiles.append(tuple(int(elem) for elem in line.split(',')))
    biggest = 0
    for i, tile1 in enumerate(tiles):
        for tile2 in tiles[i + 1:]:
            if abs((tile2[0] - tile1[0]) * (tile2[1] - tile1[1])) > biggest:
                res = (abs(tile2[0] - tile1[0]) + 1) * (abs(tile2[1] - tile1[1]) + 1)
                biggest = abs((tile2[0] - tile1[0]) * (tile2[1] - tile1[1]))

print(res)
