
grid = []
with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if (len(line) == 0):
            continue
        grid += [['.'] + list(line) + ['.']]

grid = [['.'] * len(grid[0])] + grid
grid += [['.'] * len(grid[0])]


res = 0
this_round = True
while (this_round):
    this_round = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            if (grid[i][j] != '@'):
                continue
            if sum([1 if grid[i + di][j + dj] == '@' else 0 for di in range(-1, 2) for dj in range(-1, 2)]) < 5:
                grid[i][j] = '.'
                this_round += 1;
    res += this_round
print(res)
