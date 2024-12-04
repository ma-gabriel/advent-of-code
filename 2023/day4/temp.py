
file = open("temp.txt", mode='r')

total = 0
for _ in range(213):
    gagnants = list()
    ligne = file.readline()
    ligne = ligne[9:]
    for i in range(0, 30, 3):
        gagnants.append(int(ligne[i:i+3:]))
    card = 0;
    for i in range(33, 108, 3):
        if int(ligne[i:i+3:]) in gagnants and card == 0:
                card = 1
        elif int(ligne[i:i+3:]) in gagnants:
            card *= 2;
    total += card
print(total)

file.close()
