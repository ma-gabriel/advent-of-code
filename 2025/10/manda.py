def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

res = 0
with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        lights, *buttons, joltage = line.split()
        lights = [False if light == '.' else True for light in lights[1:-1]]
        buttons = tuple(tuple(int(elem) for elem in button[1:-1].split(',')) for button in buttons)

        init_lights = [light for light in lights]
        lowest = 100000
        for n in range(1 << len(buttons)):
            temp = countSetBits(n)
            if temp >= lowest:
                continue
            for i in range(len(buttons)):
                if n & (1 << i):
                    for toggle in buttons[i]:
                        lights[toggle] = not lights[toggle]
            if not any(lights):
                lowest = temp
            lights = [light for light in init_lights]
        res += lowest
print(res)
