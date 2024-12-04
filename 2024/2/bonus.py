

def safe(lst):
    diff = 1
    if lst[1] < lst[0]:
        diff = -1
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] <= 0 and diff == 1:
            return 0
        if lst[i + 1] - lst[i] >= 0 and diff == -1:
            return 0
        if abs(lst[i + 1] - lst[i]) > 3:
            return 0
    return 1

res = 0
with open("entry.txt") as my_file:
    for line in my_file:
        
        tmp = safe([int(elem) for elem in line.split()])
        if tmp == 1:
            res += tmp
        else:
            for i in range(len(line.split())):
                stamp = [int(elem) for elem in line.split()]
                stamp.pop(i)
                if (safe(stamp)):
                    res += 1
                    break
print(res)
