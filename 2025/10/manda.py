
res = 0
with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        lights, *buttons, joltage = line.split()
        lights = [False if light == '.' else True for light in lights[1:-1]]
        buttons = tuple(tuple(int(elem) for elem in button[1:-1:2]) for button in buttons)

        init_lights = [light for light in lights]
        lowest = 100000
        for n in range(2 ** len(buttons)):
            temp = 0
            for i in range(len(buttons)):
                if n & (2 ** i):
                    for toggle in buttons[i]:
                        lights[toggle] = not lights[toggle]
                    temp += 1
            if not any(lights):
                lowest = min(lowest, temp)
            lights = [light for light in init_lights]
        res += lowest
print(res)
