import re

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

#mapSizeI = 7
mapSizeI = 103
#mapSizeJ = 11
mapSizeJ = 101

animMap = [[' ' for _ in range(mapSizeJ)] for _ in range(mapSizeI)]
robots = []


def printArray(arr):
    for row in arr:
        print(''.join(list(map(str, (row)))))

def findLongestSequence():
    longest = 0
    for i in range(len(animMap)):
        longestJ = 0
        for j in range(len(animMap[0])):
            if animMap[i][j] != ' ':
                longestJ += 1
                if longestJ > longest:
                    longest = longestJ
            else:
                longestJ = 0
    if longest > 10:
        return True
    else: return False
    

def animate():
    tick = 0
    while True:
        for rob in robots:
            rob.tick()
        tick += 1
        l = findLongestSequence()
        if l:
            printArray(animMap)     
            print(tick)
            exit()
        
        print(f'{tick}')
            

class Robot():
    
    def __init__(self, i, j, vi, vj):
        self.i = i
        self.j = j
        self.vi = vi
        self.vj = vj
        if animMap[self.i][self.j] == ' ':
            animMap[self.i][self.j] = 1
        else:
            animMap[self.i][self.j] += 1

    def tick(self):
        viCount = 0
        viInc = 0
        if animMap[self.i][self.j] == 1:
            animMap[self.i][self.j] = ' '
        else:
            animMap[self.i][self.j] -= 1

        if self.vi > 0:            
            viInc = 1
        else:
            viInc = -1

        while viCount != self.vi:
            viCount += viInc
            newI = self.i + viInc
            if newI < 0:
                self.i = mapSizeI -1
            elif newI >= mapSizeI:
                self.i = 0
            else:
                 self.i = newI


        vjCount = 0
        vjInc = 0
        if self.vj > 0:            
            vjInc = 1
        else:
            vjInc = -1
        
        while vjCount != self.vj:
            vjCount += vjInc
            newJ = self.j + vjInc
            if newJ < 0:
                self.j = mapSizeJ -1
            elif newJ >= mapSizeJ:
                self.j = 0
            else:
                 self.j = newJ
        
        if animMap[self.i][self.j] == ' ':
            animMap[self.i][self.j] = 1
        else:
            animMap[self.i][self.j] += 1
    
    def __str__(self):
        return f"i: {self.i} j: {self.j} vi: {self.vi} vj: {self.vj}"


for i, line in enumerate(file.readlines()):
    positions = re.findall('[-]?\d+', line)
    robots.append(Robot(int(positions[1]), int(positions[0]), int(positions[3]), int(positions[2])))

animate()