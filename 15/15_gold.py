file = open(__file__ + '\\..\\testInput.txt', 'r')
#file = open(__file__ + '\\..\\input.txt', 'r')
insInc = 0

def printArray(arr):
    for row in arr:
        print(''.join(row))


def findEmptySlotInLeftRight(dir, i, j):
    if dir == '<':
        j = j - 1
    elif dir == '>':
        j = j + 1
    if j < 0 or j >= len(inputMap[i]) or inputMap[i][j] == '#':
        return False

    if inputMap[i][j] == '.':
        return [i, j]
    
    return findEmptySlotInLeftRight(dir, i, j)    



def canMoveUpOrDown(ci, cj, inc):
    i = ci + inc
    print(f"mapCi {inputMap[ci][cj]} mapI {inputMap[i][cj]} ci {ci} cj: {cj}")
    if i < 0 or i >= len(inputMap) or inputMap[i][cj] == '#':
        return False
    boxPos = []
    if inputMap[ci][cj] == '.':
        return True
    
    if inputMap[i][cj] == '[':
        boxPos = [[i, cj], [i, cj + 1]]
    elif inputMap[i][cj] == ']':
        boxPos = [[i, cj - 1], [i, cj]]
    else:
        boxPos = [[i, cj], [i, cj]]

    nextJ1 = boxPos[0][1]
    nextI = i + inc
    nextJ2 = boxPos[1][1]
    print(f"map {inputMap[ci][cj]} ci {ci} cj: {cj} box: {boxPos}")    

    if inputMap[nextI][nextJ1] == '.' and inputMap[nextI][nextJ2] == '.':
        return True
    if inputMap[nextI][nextJ1] == '#' or inputMap[nextI][nextJ2] == '#':
        return False

    res1 = canMoveUpOrDown(boxPos[0][0], boxPos[0][1], inc)
    res2 = canMoveUpOrDown(boxPos[1][0], boxPos[1][1], inc)
    if insInc == 309:
        print(f"box {inputMap[nextI][nextJ1]} box2 {inputMap[nextI][nextJ2]} res1: {res1} res2: {res2}")    
        # exit()
    return res1 and res2

def pushUpDown(ci, cj, inc):

    i = ci + inc
    if inputMap[i][cj] == '[':
        boxPos = [[i, cj], [i, cj + 1]]
    elif inputMap[i][cj] == ']':
        boxPos = [[i, cj - 1], [i, cj]]
    else:
        boxPos = [[i, cj], [i, cj]]


    nextJ1 = boxPos[0][1]
    nextI = i + inc
    nextJ2 = boxPos[1][1]
    print(f"i: {i} nextI: {nextI} nextJ1: {nextJ1} nextJ2: {nextJ2}")
    print(inputMap[nextI][nextJ1])
    print(inputMap[nextI][nextJ2])
    if inputMap[nextI][nextJ1] == '.' and inputMap[nextI][nextJ2] == '.':
        inputMap[nextI][nextJ1] = inputMap[i][nextJ1]
        inputMap[nextI][nextJ2] = inputMap[i][nextJ2]
        inputMap[i][nextJ1] = '.'
        inputMap[i][nextJ2] = '.'
        return True

    print(f"PUSH 1: {boxPos[0][0]} j: {boxPos[0][1]}")
    pushUpDown(boxPos[0][0], boxPos[0][1], inc)
    #print(f"PUSH 2: {boxPos[1][0]} j: {boxPos[1][1]}")
    #pushUpDown(boxPos[1][0], boxPos[1][1], inc)

    if inputMap[nextI][nextJ1] == '.' and inputMap[nextI][nextJ2] == '.':
        inputMap[nextI][nextJ1] = inputMap[i][nextJ1]
        inputMap[nextI][nextJ2] = inputMap[i][nextJ2]
        inputMap[i][nextJ1] = '.'
        inputMap[i][nextJ2] = '.'

    





def pushLeftRight(sj, ej, inc, mapI):
    j = sj
    while j != ej:
        inputMap[mapI][j] = inputMap[mapI][j+inc]
        j+=inc
    inputMap[mapI][j] = '.'


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

    if inputMap[nI][nJ] == '.':
        inputMap[nI][nJ] = '@'
        inputMap[curI][curJ] = '.'
        return [nI, nJ]
    
    if inputMap[nI][nJ] == '#':
        return [curI, curJ]

    if inputMap[nI][nJ] == '[' or inputMap[nI][nJ] == ']':
        
        if dir == '<':
            emptySlot = findEmptySlotInLeftRight(dir, nI, nJ)
            if emptySlot == False:
                return [curI, curJ]
            pushLeftRight(emptySlot[1], curJ, 1, curI)
        elif dir == '>':
            emptySlot = findEmptySlotInLeftRight(dir, nI, nJ)
            if emptySlot == False:
                return [curI, curJ]
            pushLeftRight(emptySlot[1], curJ, -1, curI)
        elif dir == '^':
            canMove = canMoveUpOrDown(curI, curJ, -1)
            if canMove == False:
                return [curI, curJ]
            print(canMove)
            pushUpDown(curI, curJ, -1)
            inputMap[nI][nJ] = '@'
            inputMap[curI][curJ] = '.'
        elif dir == 'v':
            canMove = canMoveUpOrDown(curI, curJ, 1)
            if canMove == False:
                return [curI, curJ]
            print(canMove)
            pushUpDown(curI, curJ, 1)
            inputMap[nI][nJ] = '@'
            inputMap[curI][curJ] = '.'
           
            
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
        inputMap.append(list(line))
    else:
        line = line.removesuffix('\n')
        inst += line

#make map wider
inputMapWide = []
for i in range(len(inputMap)):
    line = ''
    for j in range(len(inputMap[i])):
        element = inputMap[i][j]
        if element == '@':
            nE = '@.'
        elif element == 'O':
            nE = '[]'
        else:
            nE = element + element
        line += nE
        
    inputMapWide.append(list(line))
    if '@' in line:
        startI = i
        startJ = line.index('@')

inputMap = inputMapWide
printArray(inputMapWide)


inst = list(inst)
curI = startI
curJ = startJ
for dir in inst:
    print(dir)
    print (insInc)
    pos = move(dir, curI, curJ)
    insInc += 1
    curI = pos[0]
    curJ = pos[1]
    printArray(inputMap)
    print('\n\n')



#caluculate result
result = 0
for i in range(len(inputMap)):
    for j in range(len(inputMap[i])):
        if inputMap[i][j] == '[':
            result += 100 * i + j

print(result)