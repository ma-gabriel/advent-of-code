
orientation = 50
res = 0

with open("entry.txt") as my_file:
    for line in my_file:
        if len(line) == 1:
            continue
        if line[0] == 'L':
            orientation -= int(line[1:]);
        else:
            orientation += int(line[1:]);
        orientation = orientation % 100
        if orientation == 0:
            res += 1;

print(res)
