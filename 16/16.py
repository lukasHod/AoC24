import sys

file = open(__file__ + '\\..\\testInput.txt', 'r')
#file = open(__file__ + '\\..\\input.txt', 'r')

sys.setrecursionlimit(10000)

dirs = {'d': [1,0], 'u': [-1,0],'r': [0,1], 'l': [0,-1]}
result = []
def printArray(arr):
    print('\n\n')
    for row in arr:
        print(row)


def move(maze: list, i, j, prevDir, turns, steps, path):
    
    for d in dirs:
        if prevDir == 'd' and d == 'u': continue
        if prevDir == 'u' and d == 'd': continue
        if prevDir == 'l' and d == 'r': continue
        if prevDir == 'r' and d == 'l': continue
            
        nI = dirs[d][0] + i
        nJ = dirs[d][1] + j

        mazeVal = maze[nI][nJ]
        if mazeVal == 'E':
            result.append(turns * 1000 + steps)
            return
        if mazeVal == '#': continue

        nt = turns
        if prevDir != d:
            nt = turns + 1
        value = turns * 1000 + steps

        if mazeVal == '.' or mazeVal > value:
            maze[nI][nJ] = value
            move(maze, nI, nJ, d, nt, steps + 1, path + f'{prevDir}:{d} ')
        
        

inputMap = []
startI = -1
startJ = -1
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    if 'S' in line:
        startI = i
        startJ = line.index('S')
        
    inputMap.append(list(line))
inputMap[startI][startJ] = 1
move(inputMap, startI, startJ, 'r', 0, 1, '')

result.sort()
print(result)