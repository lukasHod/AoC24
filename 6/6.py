#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')


map = []
startI = 0
startJ = 0

direction = "U"

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

res = go(map, startI, startJ)
while True:
    if res == "END":
        break
    res = go(map, res[0], res[1])


visits = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "X":
            visits += 1
print(visits)