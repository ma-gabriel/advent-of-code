
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
            line = line.replace(' ', '0')
            inputs.append(line)
            continue
        inputs = list(zip(*inputs))
        final = [[]]
        for i in range(len(inputs)):
            if not any([int(num) for num in inputs[i]]):
                final.append([])
            else:
                final[-1].append(int(''.join(inputs[i]).replace('0', '')))
        for i, symbol in enumerate(line.split()):
            if symbol == '*':
                res += math.prod([(num) for num in final[i]])
            elif symbol == '+':
                res += sum([int(num) for num in final[i]])
        break
print(res)
