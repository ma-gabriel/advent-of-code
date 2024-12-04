file = open("day7val.txt")
 
 
liste = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
 
def points(main, leste = {'A':1, 'K':1, 'Q':1, 'J':1, 'T':1, '9':1, '8':1, '7':1, '6':1, '5':1, '4':1, '3':1, '2':1}, liste =  ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']):
	res = { i: 0 for (i, j) in leste.items()}
	temp = 0
	for i in main:
		res[i] += 1
	res2 = {i: j for (i,j) in res.items()  if j > 1 }
	if 5 in res2.values():
		temp += 10000000000000000000000
	elif 4 in res2.values():
		temp += 1000000000000000000000
	elif 3 in res2.values() and 2 in res2.values():
		temp += 100000000000000000000
	elif 3 in res2.values():
		temp += 10000000000000000000
	elif 2 in res2.values() and len(res2.values()) == 2:
		temp += 1000000000000000000
	elif 2 in res2.values():
		temp += 100000000000000000
	for i in range(len(main)):
		temp += 13 ** i * (13 - liste.index(main[::-1][i]))
	return temp
line = file.readline()
temp = dict()
while line:
	main = line[:5]
	bet = int(line[5:])
	if points(main) in temp:
		print('perte de donnees', main, points(main))
	temp[points(main)] = bet
	line = file.readline()
resu = list(temp.keys())
resu.sort()
totql = 0
for i in range(len(resu)):
	totql += temp[resu[i]] * (i + 1)
print(totql)
