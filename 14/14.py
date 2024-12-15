import re


#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

#mapSizeI = 7
mapSizeI = 103
#mapSizeJ = 11
mapSizeJ = 101
class Robot():
    
    def __init__(self, i, j, vi, vj):
        self.i = i
        self.j = j
        self.vi = vi
        self.vj = vj

    def tick(self):
        viCount = 0
        viInc = 0
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
    
    def __str__(self):
        return f"i: {self.i} j: {self.j} vi: {self.vi} vj: {self.vj}"

rob = Robot(4, 2, -3, 2)

robots = []


for i, line in enumerate(file.readlines()):
    positions = re.findall('[-]?\d+', line)
    robots.append(Robot(int(positions[1]), int(positions[0]), int(positions[3]), int(positions[2])))



for v in range(100):
    for rob in robots:
        rob.tick()
   
q1 = 0
q2 = 0
q3 = 0
q4 = 0
q = [0, 0, 0, 0]
for rob in robots:
    qIndex = [0,1,2,3]
    if rob.i < int(mapSizeI / 2):
        qIndex.remove(2)
        qIndex.remove(3)
    elif rob.i == int(mapSizeI / 2):
        continue
    else:
        qIndex.remove(0)
        qIndex.remove(1)

    if rob.j < int(mapSizeJ / 2):
        if 1 in qIndex:
            qIndex.remove(1)
        if 3 in qIndex:
            qIndex.remove(3)
    elif rob.j == int(mapSizeJ / 2):
        continue
    else:
        if 0 in qIndex:
            qIndex.remove(0)
        if 2 in qIndex:
            qIndex.remove(2)

    finalIndex = qIndex[0]
    q[finalIndex] += 1

print(q)
print(q[0] * q[1] * q[2] * q[3])