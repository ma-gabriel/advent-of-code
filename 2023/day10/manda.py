file = open("val.txt")

liste = list();
line = file.readline()
while (line):
    liste.append(list(line))
    line = file.readline()

for i in range(len(liste)):
    if 'S' in liste[i]:
        cooS = (i, liste[i].index('S'))

coo = [cooS[0], cooS[1]]
coob = [i for i in coo]
coot = [i for i in coob]

j = 0
while coo[0] != cooS[0] or coo[1] != cooS[1] or j == 0:
    coot = [i for i in coob]
    coob = [i for i in coo]
    j+=1
    if liste[coo[0]][coo[1]] == 'S':
        coo[0] += 1
        continue
    if liste[coo[0]][coo[1]] == '7':
        if coo[1] - 1 != coot[1]:
            coo[1] -= 1
            continue
        coo[0] += 1
        continue
    if liste[coo[0]][coo[1]] == 'J':
        if coo[0] - 1 != coot[0]:
            coo[0] -= 1
            continue
        coo[1] -= 1
        continue
    if liste[coo[0]][coo[1]] == 'L':
        if coo[1] + 1 != coot[1]:
            coo[1] += 1
            continue
        coo[0] -= 1
        continue
    if liste[coo[0]][coo[1]] == '|':
        if coo[0] - 1 != coot[0]:
            coo[0] -= 1
            continue
        coo[0] += 1
        continue
    if liste[coo[0]][coo[1]] == '-':
        if coo[1] - 1 != coot[1]:
            coo[1] -= 1
            continue
        coo[1] += 1
        continue
    if liste[coo[0]][coo[1]] == 'F':
        if coo[0] + 1 != coot[0]:
            coo[0] += 1
            continue
        coo[1] += 1
        continue
    print(liste[coo[0]][coo[1]]);

print(j / 2)
