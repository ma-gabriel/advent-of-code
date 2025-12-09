
print("takes 30 seconds to run on the (slow) computer of the guy who wrote that. Be patient")

with open("entry.txt") as my_file:
    tiles = []
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        tiles.append(tuple(int(elem) for elem in line.split(',')))

    nb = len(tiles)
    biggest = 0
    res = ((-1, -1), (-1, -1))
    for i, tile1 in enumerate(tiles):
        for j, tile2 in enumerate(tiles[i + 1:]):
            if abs((tile2[0] - tile1[0]) * (tile2[1] - tile1[1])) > biggest:
                for i, tile in enumerate(tiles):
                    if len({tile1, tile2, tiles[i], tiles[(i + 1) % nb]}) == 2:
                        continue
                    if tiles[i][0] != tiles[(i + 1) % nb][0] and min(tile1[1], tile2[1]) < tile[1] < max(tile1[1], tile2[1]) and  min(tiles[i][0], tiles[(i + 1) % nb][0]) <= min(tile1[0], tile2[0]) and max(tiles[i][0], tiles[(i + 1) % nb][0]) >= max(tile1[0], tile2[0]):
                        break
                    if tiles[i][1] != tiles[(i + 1) % nb][1] and min(tile1[0], tile2[0]) < tile[0] < max(tile1[0], tile2[0]) and min(tiles[i][1], tiles[(i + 1) % nb][1]) <= min(tile1[1], tile2[1]) and max(tiles[i][1], tiles[(i + 1) % nb][1]) >= max(tile1[1], tile2[1]):
                        break
                    if min(tile1[0], tile2[0]) < tile[0] < max(tile1[0], tile2[0]) and min(tile1[1], tile2[1]) < tile[1] < max(tile1[1], tile2[1]): 
                        break
                else: 
                    biggest = abs((tile2[0] - tile1[0]) * (tile2[1] - tile1[1]))
                    res = (tile1, tile2)

print((abs(res[1][0] - res[0][0]) + 1) * (abs(res[1][1] - res[0][1]) + 1))
