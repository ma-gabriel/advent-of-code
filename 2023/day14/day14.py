file = open("valu.txt")

lst = list()
while (line := file.readline()):
	lst.append(list(line[:-1]))

'''

234 = 283

'''
for u in range(1000000000):
	for _ in lst:
		for i in range(len(lst)):
			for j in range(len(lst[0])):
				if i and lst[i][j] == 'O' and lst[i - 1][j] == '.':
					lst[i][j] = '.'
					lst[i - 1][j] = 'O'
	for _ in lst:
		for i in range(len(lst)):
			for j in range(len(lst[0])):
				if j and lst[i][j] == 'O' and lst[i][j - 1] == '.':
					lst[i][j] = '.'
					lst[i][j - 1] = 'O'

	for _ in lst:
		for i in range(len(lst)):
			for j in range(len(lst[0])):
				if i != len(lst) - 1 and lst[i][j] == 'O' and lst[i + 1][j] == '.':
					lst[i][j] = '.'
					lst[i + 1][j] = 'O'
	for _ in lst:
		for i in range(len(lst)):
			for j in range(len(lst[0])):
				if j != len(lst[0]) - 1 and lst[i][j] == 'O' and lst[i][j + 1] == '.':
					lst[i][j] = '.'
					lst[i][j + 1] = 'O'

	'''print()
	for ls in lst:
		print(ls)'''
	res = 0
	for i in range(len(lst)):
		for j in range(len(lst[0])):
			if lst[i][j] == 'O':
				res += len(lst) - i

	print(res, u)