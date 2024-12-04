
#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')


def findWord(search: str, map: list, startI: int, startJ: int):
    searchLen = len(search) - 1
    firstLetter = search[0]
    result = 0
    if (map[startI][startJ]) != firstLetter:
        return 0
    
    up = startI - searchLen >= 0
    down = startI + searchLen < len(map)
    left = startJ - searchLen >= 0
    right = startJ + searchLen < len(map[startI])
    ul = up and left
    dl = down and left
    ur = up and right
    dr = down and right

    for i in range(searchLen + 1):
        if up:
            if map[startI - i][startJ] != search[i]:
                up = False
        if down:
            if map[startI + i][startJ] != search[i]:
                down = False
        if left:
            if map[startI][startJ - i] != search[i]:
                left = False
        if right:
            if map[startI][startJ + i] != search[i]:
                right = False
        if ul:
            if map[startI - i][startJ - i] != search[i]:
                ul = False
        if dl:
            if map[startI + i][startJ - i] != search[i]:
                dl = False
        if ur:
            if map[startI - i][startJ + i] != search[i]:
                ur = False
        if dr:
            if map[startI + i][startJ + i] != search[i]:
                dr = False
    
    if up: result += 1
    if down: result += 1
    if left: result += 1
    if right: result += 1
    if ul: result += 1
    if dl: result += 1
    if ur: result += 1
    if dr: result += 1

    return result


map = []
for line in file.readlines():
    line = line.removesuffix("\n")
    lineList = [*line]
    map.append(lineList)

result = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        result += findWord("XMAS", map, i, j)
        
print(result)