file = open("val.txt")
 
liste = list()
while (line :=file.readline()):
	liste.append(list(line[:-1]))
liste[-1].append('.')
 
 
doubler = list()
for i in range(len(liste)):
	if not '#' in liste[i]:
		doubler.append(i)
 
doubleur = list()
for j in range(len(liste[0])):
	d = 1
	for i in range(len(liste)):
		if '#' == liste[i][j]:
			d = 0
	if d:
		doubleur.append(j)
 
count = 0
for i in liste:
	for j in range(len(i)):
		if i[j] == '#':
			i[j] = str(count)
			count += 1
 
def finder(carte, char):
	for i in range(len(carte)):
		if char in carte[i]:
			return (i, carte[i].index(char))
 
doubler.append(10000000)
doubleur.append(10000000)
def decoupe(a, b, doubler, doubleur):
	i1 = 0
	while doubler[i1] < min(a[0], b[0]):
		i1 += 1
	j1 = i1
	while doubler[j1] < max(a[0], b[0]):
		j1 += 1
	i2 = 0
	while doubleur[i2] < min(a[1], b[1]):
		i2 += 1
	j2 = i2
	while doubleur[j2] < max(a[1], b[1]):
		j2 += 1
	return (j1 - i1 + j2 - i2)
 
print(count * (count - 1) // 2)
print(count)
res = 0
for i in range(count):
	for j in range(i + 1, count):
		a = finder(liste, str(i))
		b = finder(liste, str(j))
		res += abs(a[0] - b[0]) + abs(a[1] - b[1])
		#res += 999999 * decoupe(a, b, doubler, doubleur) # bonus
		res += decoupe(a, b, doubler, doubleur) # manda
 
 
file.close()
print(res)
