

def nombres(i, j, carte, rec=1):
    if (rec and j <= len(carte[0]) and carte[i][j].isdigit() and carte[i][j + 1].isdigit()):
        return nombres(i, j + 1, carte)
    if (j < 0):
        return 0
    if (carte[i][j].isdigit()):
        return (int(carte[i][j]) + 10 * nombres(i, j-1, carte, rec = 0))
    return 0

file = open("carte.txt", mode='r')
carte = list()
carte.append(list(file.readline()))
while carte[-1]:
    carte.append(list(file.readline()))
carte.pop(-1)

total = 0
temp = 0
te = 0
mappa = list()
for i in range(len(carte)):
    for j in range(len(carte[0])):
        if carte[i][j] == '*':
            for k in range(-1,2):
                    for l in range(-1, 2):
                        if nombres(i + k, j + l, carte):
                            mappa.append([i,j])
                            if not temp:
                                temp = nombres(i + k, j + l, carte)
                            else :
                                te = nombres(i + k, j + l, carte) * temp
                            if i == 2 and j == 5:
                                print(nombres(i + k, j + l, carte))
                            if not (carte[i + k][j - 1].isdigit() and not carte[i + k][j].isdigit()):
                                break
            total += te
            te = 0
            temp = 0
print(mappa)
print(total)
