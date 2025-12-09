
with open("entry.txt") as my_file:
    tiles = []
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        tiles.append(tuple(int(elem) for elem in line.split(',')))
    dists = []
    for i, tile1 in enumerate(tiles):
        for tile2 in tiles[i + 1:]:
            dists.append([(abs(tile2[0] - tile1[0]) + 1) * (abs(tile2[1] - tile1[1]) + 1), tile1, tile2])
    dists.sort()

print(dists[-1][0])
