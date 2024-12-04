file = open("val.txt")

directions = file.readline()
file.readline()
line = file.readline()
dictio = dict()
while (line):
    dictio[line[:3]] = (line[7:10], line[12:15])
    line = file.readline()

temp0 = "AAA"
temp1 = "SLA"
temp2 = "PTA"
temp3 = "XJA"
temp4 = "JNA"
temp5 = "BGA"
i = j = 0

import time
while (temp0[2] != 'Z' or temp1[2] != 'Z' or temp2[2] != 'Z' or temp3[2] != 'Z' or temp4[2] != 'Z' or temp5[2] != 'Z'):
    k = directions[j] == 'R'
    temp0 = dictio[temp0][k]
    temp1 = dictio[temp1][k]
    temp2 = dictio[temp2][k]
    temp3 = dictio[temp3][k]
    temp4 = dictio[temp4][k]
    temp5 = dictio[temp5][k]
    i += 1
    j += 1
    if j == 283:
        j = 0
    if (temp0[2] == 'Z' or temp1[2] == 'Z' or temp2[2] == 'Z' or temp3[2] == 'Z' or temp4[2] == 'Z' or temp5[2] == 'Z'):
        print ( i )
        time.sleep(0.1)
print(i)

# find the PPCM of the first 6 answers of that program
