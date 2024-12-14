from time import sleep
from manda import get_robot

if __name__ == "__main__":
    robots = list()
    with open("entry.txt") as my_file:
        for line in my_file: robots.append(get_robot(line))
    width = 101
    height = 103
    seconds = 0

    print("It take less than 2 minutes, it is slow because you have to CTRL+C yourself")
    sleep(3)

    while seconds < 10000:
        seconds += 1
        floor = [[' '] * width for i in range(height)]
        for robot in robots:
            floor[(robot['i'][1] + robot['d'][1] * seconds) % height][(robot['i'][0] + robot['d'][0] * seconds) % width] = 'x'
        tmp = list()
        for line in floor:
            tmp.append(''.join(line))
        print(*tmp, sep='\n')
        print(seconds, '\n') 
        sleep(0.01)
