file = open("transition.txt")
lst = list()
boxes = dict()
res = 0;
vals = [0 for _ in range(256)]
while (line := file.readline()):
	lst.append(line[:-1])

for i in range(0, len(lst), 3):
	if lst[i][0] == '=':
		if not lst[i+2] in boxes:
			vals[int(lst[i + 1])] += 1;
			boxes[lst[i + 2]] = [ int(lst[i + 1]) + 1, vals[int(lst[i + 1])], int(lst[i][1])]
		else:
			boxes[lst[i + 2]] = [boxes[lst[i + 2]][0], boxes[lst[i + 2]][1],  int(lst[i][1])]
	elif lst[i+2] in boxes:
		vals[int(lst[i + 1])] -= 1
		slot = boxes[lst[i+2]][1]
		box = boxes[lst[i+2]][0]
		boxes.pop(lst[i+2])
		for i in boxes.keys():
			if boxes[i][0] == box and boxes[i][1] > slot:
				boxes[i][1] -= 1


print(vals)
print(boxes)
for (i, j, k) in boxes.values():
	res += i * j * k
print(res)