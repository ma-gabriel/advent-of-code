
def get_robot(line):
    space = line.find(' ')
    robot = {"i":[int(num) for num in line[line.index("=") + 1:space].split(',')]}
    line = line[space:]
    robot["d"] = [int(num) for num in line[line.index("=") + 1:].split(',')]
    return (robot)

if __name__ == "__main__":
    robots = list()
    with open("entry.txt") as my_file:
        for line in my_file: robots.append(get_robot(line))
    seconds = 100
    width = 101
    height = 103
    quadrants = [0,0,0,0]
    for robot in robots:
        coo = ((robot['i'][0] + robot['d'][0] * seconds) % width,
                (robot['i'][1] + robot['d'][1] * seconds) % height)
        if coo[0] < width // 2 and coo[1] < height // 2:
            quadrants[0] += 1
        if coo[0] > width // 2 and coo[1] < height // 2:
            quadrants[1] += 1
        if coo[0] < width // 2 and coo[1] > height // 2:
            quadrants[2] += 1
        if coo[0] > width // 2 and coo[1] > height // 2:
            quadrants[3] += 1
    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])



