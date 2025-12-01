
orientation = 50
res = 0

with open("entry.txt") as my_file:
    for line in my_file:
        if len(line) == 1:
            continue
        if line[0] == 'L':
            if (orientation == 0):
                orientation = 100
            orientation -= int(line[1:]);
        else:
            orientation += int(line[1:]);
        res += abs(orientation // 100) + (orientation % 100 == 0 if line[0] == 'L' else 0)
        orientation = orientation % 100
print(res)
