

file = open("val.txt", mode='r')

total = list()

for i in range(100):
  line = file.readline()
  red = green = blue = 0
  for _ in range(7):
    if line.find("green") != -1:
     if line[line.find("green") - 3: line.find("green") - 1].isdigit():
        if int(line[line.find("green") - 3: line.find("green") - 1]) > green:
            green = int(line[line.find("green") - 3: line.find("green") - 1])
     else: 
        if int(line[line.find("green") - 2: line.find("green") - 1]) > green:
            green = int(line[line.find("green") - 2: line.find("green") - 1])
    if line.find("blue") != -1:
     if line[line.find("blue") - 3: line.find("blue") - 1].isdigit():
        if int(line[line.find("blue") - 3: line.find("blue") - 1]) > blue:
            blue = int(line[line.find("blue") - 3: line.find("blue")  - 1])
     else:
        if int(line[line.find("blue") - 2: line.find("blue") - 1]) > blue:
            blue = int(line[line.find("blue") - 2: line.find("blue") - 1])
    if line.find("red") != -1:
     if line[line.find("red") - 3: line.find("red") - 1].isdigit():
        if int(line[line.find("red") - 3: line.find("red") - 1]) > red:
            red = int(line[line.find("red") - 3: line.find("red") - 1])
     else:
        if int(line[line.find("red") - 2: line.find("red") - 1]) > red:
            red = int(line[line.find("red") - 2: line.find("red") - 1])

    line = line[line.find(";")+1:]
  total.append(red * blue * green)
        
print(sum(total))
