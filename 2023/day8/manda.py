
file = open("val.txt")

directions = file.readline()
file.readline()
line = file.readline()
dictio = dict()
while (line):
    dictio[line[:3]] = (line[7:10], line[12:15])
    line = file.readline()

temp = "AAA"
i = 0
while (temp != "ZZZ"):
    temp = dictio[temp][directions[i % (len(directions) - 1)] =='R']
    i += 1
print(i)
