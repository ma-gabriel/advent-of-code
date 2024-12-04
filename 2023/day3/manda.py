file = open("carte.txt", mode='r')

carte = list()
carte.append(list(file.readline()))
while carte[-1]:
    carte.append(list(file.readline()))
carte.pop(-1)

def test(i, j, carte):
    if i < 0 or i >= len(carte):
        return 1
    if j < 0 or j >= len(carte[0]):
        return 1
    if carte[i][j] == '.':
        return 1
    if carte[i][j].isdigit():
        return 1
    return 0

def nombres(i, j, carte):
    if (j < 0):
        return 0
    if (carte[i][j].isdigit()):
        return (int(carte[i][j]) + 10 * nombres(i, j-1, carte))
    return 0


total = 0
pas = 0
nombre = 1
temp = list()
for i in range(len(carte)):
    for j in range(len(carte[0])):
        if carte[i][j].isdigit():
            if nombre:
                for k in range(-1,2):
                    for l in range(-1, 2):
                        if not test(i + k, j + l, carte):
                            nombre = 0
                if nombre and not carte[i][j+1].isdigit():
                    pas += nombres(i, j, carte)
                    '''temp.append([i,j])'''
        else:
            nombre = 1
            total += nombres(i, j - 1, carte)
'''
tempor = list()
for i in range(len(carte)):
    tempor.append(list())
    for j in range(len(carte[0])):
        if [i,j] in temp:
            tempor[i].append(carte[i][j])
        else:
            tempor[i].append('X')
print(tempor[-2])'''
print(total - pas - 288 - 939)
