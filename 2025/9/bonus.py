
print("takes 11 seconds to run on the (slow) computer of the guy who wrote that. Be patient")

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
                min_x = min(tile1[0], tile2[0])
                max_x = max(tile1[0], tile2[0])
                min_y = min(tile1[1], tile2[1])
                max_y = max(tile1[1], tile2[1])
                for i, tile in enumerate(tiles):
                    next_tile = tiles[(i + 1) % nb]
                    if len({tile1, tile2, tile, next_tile}) == 2:
                        continue
                    if tile[0] != next_tile[0] and min_y < tile[1] < max_y and min(tile[0], next_tile[0]) <= min_x and max(tile[0], next_tile[0]) >= max_x:
                        break
                    if tile[1] != next_tile[1] and min_x < tile[0] < max_x and min(tile[1], next_tile[1]) <= min_y and max(tile[1], next_tile[1]) >= max_y:
                        break
                    if min_x < tile[0] < max_x and min_y < tile[1] < max_y: 
                        break
                else: 
                    biggest = abs((tile2[0] - tile1[0]) * (tile2[1] - tile1[1]))
                    res = (tile1, tile2)

print((abs(res[1][0] - res[0][0]) + 1) * (abs(res[1][1] - res[0][1]) + 1))
