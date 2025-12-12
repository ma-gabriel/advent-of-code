
def backtrack(grid, which):
    if not any(which):
        return True
    mine = [i for i, x in enumerate(which) if x][0]
    which[mine] -= 1
    for i in range(len(grid) - len(presents[mine]) + 1):
        if all(grid[i]): continue
        for j in range(len(grid[i]) - len(presents[mine][0]) + 1):
            presents.append([])
            if sum([grid[i + k][j + l] for k in range(3) for l in range(3)]) > 9 - presents_len[mine]: continue 
            for _ in range(4):
                presents[mine] = list(zip(*(presents[mine])[::-1]))
                space = True
                for k in range(3):
                    for l in range(3):
                        if presents[mine][k][l] and grid[i + k][j + l]:
                            space = False
                            break
                    else:
                        continue
                    break
                if not space:
                    continue
                for k in range(3):
                    for l in range(3):
                        if presents[mine][k][l]:
                            grid[i + k][j + l] = 1
                if backtrack(grid, which):
                    return True
                for k in range(3):
                    for l in range(3):
                        if presents[mine][k][l]:
                            grid[i + k][j + l] = 0
    which[mine] += 1
    return False


print("you should really avoid reading that code.\n2025 Day 12 part 1 is special apparently, try to figure out yourself")
quit()

res = 0
with open("entry.txt") as my_file:
    presents = []
    presents_len = []
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        if line == str(len(presents)) + ':':
            presents.append([])
            presents_len.append(0)
            continue
        if ':' not in line:
            presents[-1].append([1 if char == '#' else 0 for char in line])
            presents_len[-1] += line.count('#')
            continue
        size, which = line.split(':')
        x, y = [int(num) for num in size.split('x')]
        which = [int(num) for num in which.split()]
        # works for the true output, not for the example
        if (x - x % 3) * (y - y % 3) >= sum(which) * 9:
            res += 1
        continue # AYO WHAT THE ???? WHY DOES THAT WORK ????????
        grid = [[0 for _ in range(x)] for _ in range(y)]
        tmp = backtrack(grid, which)
        print(tmp)
        res += tmp
print(res)
