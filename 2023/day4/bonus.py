
file = open("temp.txt", mode='r')

grid = list()
rows = list()
for i in range(213):
    ligne = file.readline()
    grid.append(ligne[9:])
    rows.append(1)
    
for u in range(213):
    gagnants = list()
    for i in range(0, 30, 3):
        gagnants.append(int(grid[u][i:i+3:]))
    card = 0;
    for i in range(33, 108, 3):
        if int(grid[u][i:i+3:]) in gagnants:
            card += 1
            rows[u + card] += rows[u]

print(sum(rows))
file.close()
