
def get_robot(line):
    space = line.find(' ')
    robot = {"i":[int(num) for num in line[line.index("=") + 1:space].split(',')]}
    line = line[space:]
    robot["d"] = [int(num) for num in line[line.index("=") + 1:].split(',')]
    return (robot)

def  ChristmasTree(floor):
    for i in range(len(floor)):
        if "".join(floor[i]).find("🤖" * 29) != -1:
            return True
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            floor[i][j] = '  '
    return False

if __name__ == "__main__":
    robots = list()
    with open("entry.txt") as my_file:
        for line in my_file: robots.append(get_robot(line))
    width = 101
    height = 103
    seconds = 0

    floor = [[' '] * width for i in range(height)]
    while not ChristmasTree(floor):
        seconds += 1
        for robot in robots:
            floor[(robot['i'][1] + robot['d'][1] * seconds) % height][(robot['i'][0] + robot['d'][0] * seconds) % width] = '🤖'
        if seconds == 10000:
            print("If the entry is does not work, you might have an infinite loop. My robots already formed the easter egg")

    for line in floor:
        print(''.join(line))
    print("Merry Christmas")
    print(seconds)
