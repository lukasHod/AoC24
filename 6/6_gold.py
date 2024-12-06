import copy



#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')


map = []
startI = 0
startJ = 0
obstacles = []
path = ''
direction = "U"

def printList(list):
    for listLine in list:
        print(listLine)

def putObstacle(i, j):
    map[i][j] = "#"
    obstacles.append(str(i) + "|" + str(j))


def turn():
    global direction
    if direction == "U":
        direction = "R"
    elif direction == "R":
        direction = "D"
    elif direction == "D":
        direction = "L"
    elif direction == "L":
        direction = "U"

def go(map: list, i, j):
    if direction == "U":
        if i - 1 < 0:
            return "END"
        if map[i-1][j] != "#":
            map[i-1][j] = "X"
            return [i-1, j]
        else:
            turn()
            return [i, j]
    if direction == "R":
        if j+1 > len(map[i]) -1:
            return "END"
        if map[i][j+1] != "#":
            map[i][j+1] = "X"
            return [i, j+1]
        else:
            turn()
            return [i, j]
    if direction == "D":
        if i + 1 > len(map) -1:
            return "END"
        if map[i+1][j] != "#":
            map[i+1][j] = "X"
            return [i+1, j]
        else:
            turn()
            return [i, j]
    if direction == "L":
        if j - 1 < 0:
            return "END"
        if map[i][j - 1] != "#":
            map[i][j - 1] = "X"
            return [i, j - 1]
        else:
            turn()
            return [i, j]
        


def fillX(mapCopy):
    res = go(mapCopy, startI, startJ)
    while True:
        if res == "END":
            break
        res = go(mapCopy, res[0], res[1])
    return mapCopy

i = 0
for line in file.readlines():
    line = line.removesuffix("\n")
    lineChars = list(line)
    if '^' in lineChars:
        startI = i
        startJ = lineChars.index("^")
        lineChars[startJ] = "X"

    map.append(lineChars)

    i += 1



mapX = copy.deepcopy(map)
emptyMap = copy.deepcopy(map)
mapCopy = fillX(mapX)
cycles = 0

for i in range(len(mapX)):
    for j in range(len(mapX[i])):
        if mapX[i][j] != "X": continue

        path = ""
        direction = "U"

        emptyMap[i][j] = "#"
        res = go(emptyMap, startI, startJ)
        lastI = startI
        lastJ = startJ
        while True:
            if res == "END":
                break
            res = go(emptyMap, res[0], res[1])
            if res[0] == lastI and res[1] == lastJ:
                continue

            newInst = str(res[0]) + "-" + str(res[1]) + "--"
            if  f"--{lastI}-{lastJ}--{res[0]}-{res[1]}--" in path:
                cycles += 1
                break
            path += newInst
            lastI = res[0]
            lastJ = res[1]

        
        emptyMap[i][j] = "."

print(cycles)