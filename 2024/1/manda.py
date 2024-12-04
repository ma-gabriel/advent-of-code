
col1 = []
col2 = []

with open("entry.txt") as my_file:
    for line in my_file:
        a, b = [int(elem) for elem in line.split()]
        col1.append(a)
        col2.append(b)
col1.sort()
col2.sort()

res = 0
for i in range(len(col1)):
    res += abs(col1[i] - col2[i])
print(res)
