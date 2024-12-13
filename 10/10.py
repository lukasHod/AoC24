import copy



#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')
result = []

class Point:
    def __init__(self, i, j, v):
        self.i = i
        self.j = j
        self.v = v
        self.n = []
        self.score = 0
        self.prevN = 0
    
    def getI(self):
        return self.i

    def getJ(self):
        return self.j
    
    def getNeibours(self):
        return self.n
    
    def addNeibour(self, newPoint):
        self.n.append(newPoint)

    def getValue(self):
        return self.v
    
    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score
    
    def setPrevN(self, prevNeighbour):
        self.prevN = prevNeighbour

    def getPrevN(self):
        return self.prevN
    
    def __str__(self) -> str:
        return f"i:{self.i} j:{self.j} value: {self.v} score: {self.score}"


        
def goForAWalk(point: Point, hikeMap, startPoint: Point):
    directions = [
        [-1, 0,],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    pointI = point.getI()
    pointJ = point.getJ()
    if int(hikeMap[pointI][pointJ]) == 9:
        hikeMap[pointI][pointJ] = '.'
        startPoint.setScore(startPoint.getScore() + 1)
        return
    #print('--------------------------------------')
    for d in directions:
        if (
            pointI + d[0] < 0 or 
            pointI + d[0] >= len(hikeMap) or 
            pointJ + d[1] < 0 or
            pointJ + d[1] >= len(hikeMap[0])

        ):
            continue
        pI = pointI + d[0]
        pJ = pointJ + d[1]
        if hikeMap[pI][pJ] == '.':
            continue

        #print(f"mapVal: {hikeMap[pI][pJ]} pI: {pI} pJ: {pJ} direction: {d}")

        

        if int(hikeMap[pI][pJ]) == point.getValue() + 1:
            #print('right dir')
            #print(point.getPrevN())
            if  point.getPrevN() == 0 or (point.getPrevN().getI() != pI or point.getPrevN().getJ() != pJ):
                newPoint = Point(pI, pJ, int(hikeMap[pI][pJ]))
                newPoint.setPrevN(point)
                point.addNeibour(newPoint)
        
    
    #print(point.getNeibours())
    if len(point.getNeibours()) == 0:
        return 0
    
    for n in point.getNeibours():
        goForAWalk(n, hikeMap, startPoint)



def printArray(listMap):
    for m in listMap:
        print(m)

hikeMap = []
startPoints = []

for i, line in enumerate(file.readlines()):
    line = list(line.removesuffix("\n"))
    for j, l in enumerate(line):
        if l == '0':
            point = Point(i, j, 0)
            startPoints.append(point)
    hikeMap.append(line)
    

#printArray(hikeMap)
#printArray(startPoints)

for sp in startPoints:
    hikeMapCopy = copy.deepcopy(hikeMap)
    goForAWalk(sp, hikeMapCopy, sp)
    result.append(sp.getScore())


print(sum(result))
