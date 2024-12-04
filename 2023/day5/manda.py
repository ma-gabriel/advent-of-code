file = open("temp.txt", mode='r')

leste = set()
ligne = file.readline()
ligne = ligne[7:]
for _ in range(20):
    i = 0
    while ligne[i].isdigit() and i + 1 < len(ligne):
        i+= 1
    leste.add(int(ligne[:i]))
    ligne = ligne[i + 1:]


print(leste)
temp = set()

for _ in range(226):
 ligne = file.readline()
 if ligne[:1].isdigit():
    i = 0
    while ligne[i].isdigit():
        i+= 1
    dest = int(ligne[:i])
    ligne = ligne[i:]
    i = 1
    while ligne[i].isdigit():
        i+= 1
    src = int(ligne[:i])
    ligne = ligne[i:]
    rang = int(ligne)
    i = 0;
    for numbers in list(leste):
        if src < numbers < src + rang:
            temp.add(dest + numbers - src)
            leste.remove(numbers)
 else:
     leste = leste | temp
     temp = set()

leste = leste | temp

print(min(list(leste)))

file.close()
