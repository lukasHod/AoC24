


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



for line in file.readlines():
    line = list(line.removesuffix("\n"))
    dotLine = list(createDotLine(line))

    endI = len(dotLine) -1
    for i, char in enumerate(dotLine):
        if i > endI:
            break
        if char != '.': continue

        newVal = ''
        while True:
            if dotLine[endI] == '.':
                endI -= 1
            elif i > endI:
                break
            else:
                newVal = dotLine[endI]
                dotLine[endI] = '.'
                endI -= 1
                break
        if newVal != '':
            dotLine[i] = newVal

#    print(''.join(dotLine)[194500:195500])

    checkSum = 0
    for i, val in enumerate(dotLine):
        if val == '.': break
        checkSum += (i * int(val))
    print(checkSum) # 6344673854800
