file = open("val.txt")
 
def func(line):
    linebis = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    if len(set(linebis)) != 1 or linebis[0] != 0:
        func(linebis)
        line.append(linebis[-1] + line[-1])
        return(line[-1])
 
 
res = 0
line = file.readline()
while (line):
    line = line.split()
    line = [int(i) for i in line]
    res += func(line)
    #res += func(line[::-1])  #uncomment that and comment the above for the bonus
    line = file.readline()
print(res)
 
 
file.close()
