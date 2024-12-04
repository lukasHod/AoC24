
file = open(__file__ + '\\..\\testInput.txt', 'r')
#file = open(__file__ + '\\..\\input.txt', 'r')

allcombos = [
    "MSAMS",
    "MMASS",
    "SSAMM",
    "SMASM"
]

def findWord(map: list, startI: int, startJ: int):
    if (map[startI][startJ]) != "A":
        return 0
    
    if startI - 1 < 0 or startI + 1 >= len(map) or startJ - 1 < 0 or startJ + 1 >= len(map[startI]):
        return 0

    text = map[startI - 1][startJ - 1] + map[startI - 1][startJ + 1] + "A" + map[startI + 1][startJ - 1] + map[startI + 1][startJ + 1]
    if text in allcombos:
        return 1

    return 0

map = []
for line in file.readlines():
    line = line.removesuffix("\n")
    lineList = [*line]
    map.append(lineList)

result = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        result += findWord(map, i, j)
        
print(result)