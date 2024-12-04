

res = 0
for i in range(47986698):
    vitesse = i
    distance = vitesse * (47986698 - i)
    if distance > 400121310111540:
        res += 1

print(res)
