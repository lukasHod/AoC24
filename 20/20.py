import copy

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')



inputMap = []
startI = -1
startJ = -1
eI = -1
eJ = -1
crosses = {}
path = []

def printArray(arr):
    print('\n\n')
    for row in arr:
        rs = map(str, row)
        print(''.join(rs))

def setStepNumbers(maze: list, startI, startJ, endI, endJ):
    #print(f"startI: {startI}, startJ: {startJ}, endI: {endI}, endJ: {endJ}")
    directions = {'r': (0, 1), 'd':(1, 0), 'l': (0, -1), 'u': (-1, 0)}  # Right, Down, Left, Up
    maze[startI][startJ] = 1
    path.append((startI, startJ))
    i, j = startI, startJ
    steps = 2

    while maze[i][j] != 'E':
        for d in directions:
            di, dj = directions[d][0], directions[d][1]
            ni, nj = i + di, j + dj
            
            if maze[ni][nj] == '.' or maze[ni][nj] == 'E':
                maze[ni][nj] = steps
                steps += 1
                i = ni
                j = nj
                pos = (i, j)
                path.append(pos)
                break
        #print(f"i: {i} j: {j}")
        if i == endI and j == endJ:
            break

def tryCross(maze, i, j):
    longDirections = {'r': (0, 2), 'd':(2, 0), 'l': (0, -2), 'u': (-2, 0)}  # Right, Down, Left, Up
    shortDirections = {'r': (0, 1), 'd':(1, 0), 'l': (0, -1), 'u': (-1, 0)}  # Right, Down, Left, Up
    
    
    for d in longDirections:
        di, dj = longDirections[d][0], longDirections[d][1]
        ni, nj = i + di, j + dj

        if ni < 0 or nj < 0 or ni >= len(maze) or nj >= len(maze[ni]):
            continue
        if maze[ni][nj] == '#':
            continue
        
        if maze[i][j] > maze[ni][nj]:
            continue
        
        sdi, sdj = shortDirections[d][0], shortDirections[d][1]
        si, sj = i + sdi, j + sdj
        if maze[si][sj] != '#':
            continue

        crosPos = f"{si}:{sj}"
        crosses[crosPos] = maze[ni][nj] - maze[i][j] - 2


for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    inputMap.append(list(line))
    if 'S' in line:
        startI = i
        startJ = line.index('S')
    if 'E' in line:
        eI = i
        eJ = line.index('E')

originMap = copy.deepcopy(inputMap)

setStepNumbers(inputMap, startI, startJ, eI, eJ)

for p in path:
    tryCross(inputMap, p[0], p[1])

all = 0
for c in crosses:
    if crosses[c] >= 100:
        all += 1
print(all) # < 5476