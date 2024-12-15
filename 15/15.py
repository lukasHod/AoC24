#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

def printArray(arr):
    for row in arr:
        print(row)


def findEmptySlotInDir(dir, i, j):
    if dir == '<':
        j = j - 1
    elif dir == '>':
        j = j + 1
    elif dir == '^':
        i = i - 1
    elif dir == 'v':
        i = i + 1
    else:
        print('bad input')
        exit()
    if i < 0 or j < 0 or i >= len(inputMap) or j >= len(inputMap[i]) or inputMap[i][j] == '#':
        return False

    if inputMap[i][j] == '.':
        return [i, j]
    
    return findEmptySlotInDir(dir, i, j)    


def move(dir, curI, curJ):
    nJ = curJ
    nI = curI
    if dir == '<':
        nJ = curJ - 1
    elif dir == '>':
        nJ = curJ + 1
    elif dir == '^':
        nI = curI - 1
    elif dir == 'v':
        nI = curI + 1
    else:
        print('bad input')
        exit()

    if inputMap[nI][nJ] == '.':
        inputMap[nI][nJ] = '@'
        inputMap[curI][curJ] = '.'
        return [nI, nJ]
    
    if inputMap[nI][nJ] == '#':
        return [curI, curJ]

    if inputMap[nI][nJ] == 'O':
        emptySlot = findEmptySlotInDir(dir, nI, nJ)
        if emptySlot == False:
            return [curI, curJ]
        inputMap[emptySlot[0]][emptySlot[1]] = 'O'
        inputMap[curI][curJ] = '.'
        inputMap[nI][nJ] = '@'
            
    return [nI, nJ]

inputMap = []
firstPart = True
inst = ''
startI = -1
startJ = -1
for i, line in enumerate(file.readlines()):
    if line == '\n':
        firstPart = False
        continue
    if firstPart:
        line = line.removesuffix('\n')
        if '@' in line:
            startI = i
            startJ = line.index('@')
        inputMap.append(list(line))
    else:
        line = line.removesuffix('\n')
        inst += line
inst = list(inst)
curI = startI
curJ = startJ

for dir in inst:
    pos = move(dir, curI, curJ)
    curI = pos[0]
    curJ = pos[1]


result = 0
for i in range(len(inputMap)):
    for j in range(len(inputMap[i])):
        if inputMap[i][j] == 'O':
            result += 100 * i + j

print(result)