file = open("valu.txt")


def chiant(lst, val):
    if (len(lst) == val):
        return 1
    if lst[val] != '#':
        return 0
    return 1

def backtrack(lst, vals, inter = 0):
    res  = 0;
    if not len(vals) and not '#' in lst: 
        return not inter
    if not len(vals):
        return 0
    val = vals[0]
    if not len(lst):
        return 0
    if '.' in lst[:val]:
        print(1)
        pass
    elif (len(vals) == 1 and len(lst) == val and not '.' in lst[:val]):
            return 1
    elif len(vals) == 1 and len(lst) >= val and not '.' in lst[:val] and not inter and chiant(lst, val) and not (lst[0] == '#'):
        return backtrack(lst[1:], vals, inter = (lst[0] == '#')) + (len(lst) == val)
    elif len(lst) < sum(vals) + len(vals) - 1:
        return res
    if not lst[0] == '#':
        res += backtrack(lst[1:], vals, inter = (lst[0] == '#'))
    if ('.' in lst[:val] or chiant(lst, val) or inter):
        return res 
    res += backtrack(lst[val + 1:], vals[1:])
    return res

res = 0
while (line := file.readline()):
    temp = line.index(' ')
    temp2 = res
    print('\n', line, end='')
    ls = list(line)[:temp] + ['?'] + list(line)[:temp] + ['?'] + list(line)[:temp] + ['?'] + list(line)[:temp] + ['?'] + list(line)[:temp]
    res += backtrack(ls, [int(i) for i in line[temp + 1: -1].split(",")]*5)
    print(res - temp2)

print(res)
