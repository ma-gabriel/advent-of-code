file = open("val.txt")
line = "sd"
res = 0
while line:
	maps = list()
	lst = set(range(-100, 100))
	
	while len(line := file.readline()) > 2:
		temp = set()
		maps.append(line[:-1])
		for i in range(len(line[:-1])):
			if line[:-1][:i]==line[:-1][i:i*2][::-1] and i:
				temp.add(i)
			if line[:-1][-2 - i * 2: - 1 - i] == line[:-1][- 1 - i::][::-1]:
				temp.add(-i)
		lst = temp & lst

	if len(lst):
		if list(lst)[0] > 0:
			res += max(list(lst))
			for i in maps:
				print(str(i))
			print(max(list(lst)), 1, max(list(lst)))
		else:
			res += (len(maps[0]) + max(list(lst))) - 1
			for i in maps:
				print(str(i))
			print((len(maps[0]) + max(list(lst))) - 1, 1, max(list(lst)))
	lst = set(range(-100, 100))
	maps = list(zip(*maps[::-1]))
	maps = list(zip(*maps[::-1]))
	maps = list(zip(*maps[::-1]))
	for lin in maps:
		temp = set()
		for i in range(len(lin)):
			if lin[:i]==lin[i:i*2][::-1] and i:
				temp.add(i)
			if lin[-2 - i * 2: - 1 - i] == lin[- 1 - i::][::-1]:
				temp.add(-i)
		lst = temp & lst
	if len(lst):
		if list(lst)[0] > 0:
			res += max(list(lst)) * 100
			for i in maps:
				print(str(i))
			print(max(list(lst)) * 100, 1, max(list(lst)))
		else:
			res += ((len(maps[0]) + max(list(lst))) - 1) * 100
			for i in maps:
				print(str(i))
			print(((len(maps[0]) + max(list(lst))) - 1) * 100, 1, max(list(lst)))
print(res)