

res = 0
for i in range(47):
    vitesse = i
    distance = vitesse * (47 - i)
    if distance > 400:
        res += 1
total = res
res = 0
for i in range(98):
    vitesse = i
    distance = vitesse * (98 - i)
    if distance > 1213:
        res += 1

total *= res
res = 0
for i in range(66):
    vitesse = i
    distance = vitesse * (66 - i)
    if distance > 1011:
        res += 1


total *= res
res = 0
for i in range(98):
    vitesse = i
    distance = vitesse * (98 - i)
    if distance > 1540:
        res += 1

print (total * res)


