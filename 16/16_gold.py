import sys
import copy

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

sys.setrecursionlimit(10000)

dirs = {'d': [1,0], 'u': [-1,0],'r': [0,1], 'l': [0,-1]}
result = []
bestPaths = []

def printArray(arr):
    print('\n\n')
    for row in arr:
        rs = map(str, row)
        print(' '.join(rs))


def calculateBestPaths():
    dictOfPos = {}
    for maze in bestPaths:
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                ijPos = f'{i}:{j}'
                if maze[i][j] == 'O' and ijPos not in dictOfPos:
                    dictOfPos[ijPos] = 1
    print(len(dictOfPos))




def checkCrossroad(maze: list, i, j, prevDir):
    res = 0
    for d in dirs:
        if prevDir == 'd' and d == 'u': continue
        if prevDir == 'u' and d == 'd': continue
        if prevDir == 'l' and d == 'r': continue
        if prevDir == 'r' and d == 'l': continue

        nI = dirs[d][0] + i
        nJ = dirs[d][1] + j 
        if maze[nI][nJ] == '.':
            res += 1
    return res

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
        value = nt * 1000 + steps

        if mazeVal == '.' or mazeVal > value:
            maze[nI][nJ] = value
            move(maze, nI, nJ, d, nt, steps + 1, path + f'{prevDir}:{d} ')

def findBestPaths(maze: list, i, j, prevDir, turns, steps, path, resultToReach):
    
    for d in dirs:
        if prevDir == 'd' and d == 'u': continue
        if prevDir == 'u' and d == 'd': continue
        if prevDir == 'l' and d == 'r': continue
        if prevDir == 'r' and d == 'l': continue

        nI = dirs[d][0] + i
        nJ = dirs[d][1] + j
        mazeVal = maze[nI][nJ]
        if mazeVal == '#' or mazeVal == 'O': continue

        nt = turns
        if prevDir != d:
            nt = turns + 1

        value = nt * 1000 + steps
        if value > resultToReach:
            return

        if mazeVal == 'E':
            maze[nI][nJ] = 'O'
            bestPaths.append(maze)
            calculateBestPaths()
            return

        if mazeVal == '.':
            copyMaze = copy.deepcopy(maze)                
            copyMaze[nI][nJ] = 'O'

            findBestPaths(copyMaze, nI, nJ, d, nt, steps + 1, path + f'{prevDir}:{d} ', resultToReach)
        
        

inputMap = []
startI = -1
startJ = -1
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    if 'S' in line:
        startI = i
        startJ = line.index('S')
        
    inputMap.append(list(line))

originMap = copy.deepcopy(inputMap)
inputMap[startI][startJ] = 1

move(inputMap, startI, startJ, 'r', 0, 1, '')
#printArray(inputMap)
result.sort()
originMap[startI][startJ] = 'O'
#print('finding')
#print(result[0]) #102460
findBestPaths(originMap, startI, startJ, 'r', 0, 1, '', 102460)


