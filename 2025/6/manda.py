
import math

res = 0
inputs = []

with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        if line[0] not in ['*', '+']:
            inputs.append([int(tmp) for tmp in line.split()])
            continue
        inputs = list(zip(*inputs[::-1]))
        for i, symbol in enumerate(line.split()):
            if symbol == '*':
                res += math.prod(inputs[i]);
            elif symbol == '+':
                res += sum(inputs[i])
        break
print(res)
