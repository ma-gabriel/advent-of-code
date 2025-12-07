import math

res = 0
inputs = []
last = None
with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = list(line[:-1])
        if len(line) == 0:
            continue
        for i in range(len(line)):
            if (line[i] == '.' or type(line[i]) is int)  and last and (last[i] == 'S' or type(last[i]) is int) :
                if last[i] == 'S':
                    line[i] = 1
                elif type(line[i]) is int:
                    line[i] += last[i]
                else:
                    line[i] = last[i]
            if line[i] == '^' and last and type(last[i]) is int:
                if type(line[i - 1]) is int:
                    line[i - 1] += last[i]
                else:
                    line[i - 1] = last[i]
                line[i + 1] = last[i]
        last = line
print(sum([elem if type(elem) is int else 0 for elem in last]))
