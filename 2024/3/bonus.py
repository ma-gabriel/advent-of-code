def atoi(s):
    result = '0'
    for char in s:
        if char.isdigit():result += char
        else:break
    return int(result)


res = 0
with open("entry.txt") as my_file:
    stop = 0
    for line in my_file:
        i = 0
        while i < len(line):

            if line[i:i+7] == "don't()" or stop:
                stop = 1
                while line[i:i+4] != "do()" and i < len(line):
                    i+=1
                if line[i:i+4] == "do()":
                    stop = 0

            if line[i:i+4] == "mul(":
                i += 4
                tmp1 = atoi(line[i:])
                if tmp1:
                    while line[i].isnumeric():i+=1
                    if line[i] == ',':
                        i+=1
                        tmp2 = atoi(line[i:])
                        if tmp2:
                            while line[i].isnumeric():i+=1
                            if line[i] == ')':
                                res += tmp1 * tmp2
            i+=1

print(res)
