
import sys
sys.setrecursionlimit(100000)

'''
0 : facing east
1 : facing north
2 : facing south
3 : facing west
'''
def intersection(maze, i, j, a, path):
    if (maze[i][j] == 'E'):
        print("+ 1 way to find the end: ", *path, (i, j), sep='')
        return 0
    if (i, j) in path or maze[i][j] == '#':
        return float('inf');
    path.append((i, j))
    tmp = [float('inf')]
    if a != 3 and maze[i][j + 1] != '#':
        tmp.append(keep(maze, i, j, 0, path=path) + 1000 * (a != 0))
    if a != 2 and maze[i - 1][j] != '#':
        tmp.append(keep(maze, i, j, 1, path=path) + 1000 * (a != 1))
    if a != 1 and maze[i + 1][j] != '#':
        tmp.append(keep(maze, i, j, 2, path=path) + 1000 * (a != 2))
    if a != 0 and maze[i][j - 1] != '#':
        tmp.append(keep(maze, i, j, 3, path=path) + 1000 * (a != 3))
    path.pop()
    return (min(tmp))

def keep(maze, i, j, a, path=list()):
    if (maze[i][j] == 'E'):
        print("+ 1 way to find the end: ", *path, sep='')
        return 0
    d = 1
    if a == 0:
        while (maze[i - 1][j + d] == '#' and maze[i + 1][j + d] == '#' and maze[i][j + d] == '.') : d += 1
        return (d + intersection(maze, i, j + d, 0, path))
    elif a == 1:
        while (maze[i - d][j - 1] == '#' and maze[i - d][j + 1] == '#' and maze[i - d][j] == '.') : d += 1
        return (d + intersection(maze, i - d, j, 1, path))
    elif a == 2:
        while (maze[i + d][j - 1] == '#' and maze[i + d][j + 1] == '#' and maze[i + d][j] == '.') : d += 1
        return (d + intersection(maze, i + d, j, 2, path))
    else:
        while (maze[i - 1][j - d] == '#' and maze[i + 1][j - d] == '#' and maze[i][j - d] == '.') : d += 1
        return (d + intersection(maze, i, j - d, 3, path))
    

def find(doc):
    for i, line in enumerate(doc):
        if 'S' in line: return i, line.index('S')

if __name__ == "__main__":
    maze = list()
    with open("entry.txt") as my_file:
        start = True
        for line in my_file:
            if '\n' in line:
                maze.append(list(line[:-1]))
            else:
                maze.append(list(line[:-1]))
    coos = find(maze)
    print(intersection(maze, *coos, 5, []) - 1000)
