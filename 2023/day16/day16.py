def gogogo(maps, coo, ener):
	while (True):
		if coo[2] == 1:
			if coo[1] + 1 == len(maps[0]) or (ener[coo[0]][coo[1] + 1] % 10):
				return
			if maps[coo[0]][coo[1] + 1] == '|':
				ener[coo[0]][coo[1] + 1] += 1
				gogogo(maps, [coo[0], coo[1] + 1, 0], ener)
				coo[1] += 1;
				coo[2] = 2;
			elif maps[coo[0]][coo[1] + 1] == '.' or maps[coo[0]][coo[1] + 1] == '-':
				coo[1] += 1;
				ener[coo[0]][coo[1]] += 1
			elif maps[coo[0]][coo[1] + 1] == '\\':
				coo[1] += 1;
				coo[2] = 2;
				ener[coo[0]][coo[1]] += 1
			elif maps[coo[0]][coo[1] + 1] == '/':
				coo[1] += 1;
				coo[2] = 0;
				ener[coo[0]][coo[1]] += 1
		elif coo[2] == 3:
			if not coo[1] or ((ener[coo[0]][coo[1] - 1] // 10) % 10):
				return
			if maps[coo[0]][coo[1] - 1] == '|':
				ener[coo[0]][coo[1] - 1] += 10
				gogogo(maps, [coo[0], coo[1] - 1, 0], ener)
				coo[1] -= 1;
				coo[2] = 2;
			elif maps[coo[0]][coo[1] - 1] == '.' or maps[coo[0]][coo[1] - 1] == '-':
				coo[1] -= 1;
				ener[coo[0]][coo[1]] += 10
			elif maps[coo[0]][coo[1] - 1] == '\\':
				coo[1] -= 1;
				coo[2] = 0;
				ener[coo[0]][coo[1]] += 10
			elif maps[coo[0]][coo[1] - 1] == '/':
				coo[1] -= 1;
				coo[2] = 2;
				ener[coo[0]][coo[1]] += 10
		elif coo[2] == 0:
			if not coo[0] or ((ener[coo[0] - 1][coo[1]] // 100) % 10):
				return
			if maps[coo[0] - 1][coo[1]] == '-':
				ener[coo[0] - 1][coo[1]] += 100
				gogogo(maps, [coo[0] - 1, coo[1], 1], ener)
				coo[0] -= 1;
				coo[2] = 3;
			elif maps[coo[0] - 1][coo[1]] == '.' or maps[coo[0] - 1][coo[1]] == '|':
				coo[0] -= 1;
				ener[coo[0]][coo[1]] += 100
			elif maps[coo[0] - 1][coo[1]] == '\\':
				coo[0] -= 1;
				coo[2] = 3;
				ener[coo[0]][coo[1]] += 100
			elif maps[coo[0] - 1][coo[1]] == '/':
				coo[0] -= 1;
				coo[2] = 1;
				ener[coo[0]][coo[1]] += 100
		elif coo[2] == 2:
			if coo[0] + 1 == len(maps) or (ener[coo[0] + 1][coo[1]] // 1000):
				return
			if maps[coo[0] + 1][coo[1]] == '-':
				ener[coo[0] + 1][coo[1]] += 1000
				gogogo(maps, [coo[0] + 1, coo[1], 1], ener)
				coo[0] += 1;
				coo[2] = 3;
			elif maps[coo[0] + 1][coo[1]] == '.' or maps[coo[0]+ 1][coo[1]] == '|':
				coo[0] += 1;
				ener[coo[0]][coo[1]] += 1000
			elif maps[coo[0] + 1][coo[1]] == '\\':
				coo[0] += 1;
				coo[2] = 1;
				ener[coo[0]][coo[1]] += 1000
			elif maps[coo[0] + 1][coo[1]] == '/':
				coo[0] += 1;
				coo[2] = 3;
				ener[coo[0]][coo[1]] += 1000

poi = 0
leste = list()
while poi < 440:
	if poi < 110:
		x = poi
		y = 0
		dir = 1
	elif poi < 220:
		x = poi - 110
		y = 109
		dir = 3
	elif poi < 330:
		x = 0
		y = poi - 220
		dir = 2
	else:
		x = 109
		y = poi - 330
		dir = 0
	file = open("val.txt")
	maps = list()


	while (line := file.readline()):
		maps.append(list(line[:-1]))

	ener = [ [0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
	ener[x][y] = 1
	coo = [x,y, dir]

	
	gogogo(maps, coo, ener)


	res = 0
	for i in ener:
		for j in i:
			if j:
				res += 1
	leste.append(res)
	file.close()
	poi += 1
print(max(leste))