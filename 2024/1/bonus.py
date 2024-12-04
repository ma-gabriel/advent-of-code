
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
for elem in col1:
    res += col2.count(elem) * elem
print(res)
