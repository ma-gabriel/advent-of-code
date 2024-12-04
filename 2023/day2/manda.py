

file = open("val.txt", mode='r')

red = 12
green = 13
blue = 14
total = 0

for i in range(100):
  game_won = i + 1
  line = file.readline()
  for _ in range(7):
    if line[line.find("green") - 3: line.find("green") - 1].isdigit():
        if int(line[line.find("green") - 3: line.find("green") - 1]) > green:
            game_won = 0
    if line[line.find("blue") - 3: line.find("blue") - 1].isdigit():
        if int(line[line.find("blue") - 3: line.find("blue") - 1]) > blue:
            game_won = 0
    if line[line.find("red") - 3: line.find("red") - 1].isdigit():
        if int(line[line.find("red") - 3: line.find("red") - 1]) > red:
            game_won = 0
    line = line[line.find(";")+1:]
  total += game_won
        
print(total)
