


#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

def createDotLine(line: list):
    dotLine = []
    index = 0
    for i, value in enumerate(line):
        if i % 2 == 0 or i == 0:
            for j in range(int(value)):
                dotLine.append(str(index))
            index += 1
        else:
            dots = list('.' * int(value))
            dotLine = dotLine + dots 
        
    return dotLine


def getFileLenAndLastIndex(dotLine, index):
    fileLen = 1

    while True:
        if dotLine[index] == '.':
            index -= 1
            continue

        #count file len
        while dotLine[index - fileLen] == dotLine[index]:
            fileLen += 1
        break
    return [fileLen, index - fileLen, index, dotLine[index]]
        
def getSpanMatchToFilelen(dotLine, fileLen, stopindex):
    startIndex = -1
    spanLen = 0
    for i, char in enumerate(dotLine):
        if i >= stopindex: return -1

        if char == '.' and startIndex == -1:
            startIndex = i

        if char == '.':
            spanLen += 1
            if spanLen >= fileLen:
                return startIndex    

        if char != '.' and startIndex != -1:
            startIndex = -1
            spanLen = 0

for line in file.readlines():
    line = list(line.removesuffix("\n"))
    dotLine = list(createDotLine(line))
    endI = len(dotLine) -1

    while endI > 0:
        end = getFileLenAndLastIndex(dotLine, endI)
        fileLen = end[0]
        endI = end[2]

        spanStartIndex = getSpanMatchToFilelen(dotLine, fileLen, endI)
        if spanStartIndex == -1:
            endI = end[1]
            continue

        for lenF in range(fileLen):
            dotLine[spanStartIndex + lenF] = dotLine[endI - lenF]
            dotLine[endI - lenF] = '.'
        
        endI = end[1]

#    print(''.join(dotLine)[194500:195500])

    checkSum = 0
    for i, val in enumerate(dotLine):
        if val != '.':
            checkSum += (i * int(val))
    print(checkSum) # > 3875374595942
