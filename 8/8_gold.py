from itertools import product
import copy

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

def printArray(map):
    for m in map:
        print(m)

def createAntinodeMap(antenas, map):
    antinodes = []
    for type in antenas:
        typeAntenas = antenas[type]
        for i in range(len(typeAntenas)):
            posA = typeAntenas[i]
            posAt = f"{posA[0]}-{posA[1]}"
            if posAt not in antinodes:
                antinodes.append(posAt)
            for j in range(len(typeAntenas)):
                if i == j: continue
                posB = typeAntenas[j]
                vectorO = [(posB[0] - posA[0]) * -1, (posB[1] - posA[1]) * -1]
                vector = [(posB[0] - posA[0]) * -1, (posB[1] - posA[1]) * -1]
                antinodePos = [posA[0] + vectorO[0], posA[1] + vectorO[1]]
                while antinodePos[0] >= 0 and antinodePos[0] < len(map) and antinodePos[1] >= 0 and antinodePos[1] < len(map[0]):
                    pos = f"{antinodePos[0]}-{antinodePos[1]}"
                    if pos not in antinodes:
                        antinodes.append(pos)
                    vector = [vector[0] + vectorO[0], vector[1] + vectorO[1]]
                    antinodePos = [posA[0] + vector[0], posA[1] + vector[1]]
    return antinodes

def drawAntinodesMap(copyMap, antinodes):
    for at in antinodes:
        pos = list(map(int, at.split('-')))
        copyMap[pos[0]][pos[1]] = '#'
    printArray(copyMap)

def createMaps():
    antenas = {}
    mapp = []
    i = 0
    for line in file.readlines():
        line = line.removesuffix("\n")
        row = list(line)
        for j in range(len(row)):
            if row[j] != '.':
                if row[j] in antenas:
                    antenas[row[j]].append([i,j])
                else:
                    antenas[row[j]] = [[i,j]]
        mapp.append(row)

        i += 1

    return [mapp, antenas]

maps = createMaps()
mapp = maps[0]
antenas = maps[1]
copyMap = copy.deepcopy(mapp)

antinodes:list = createAntinodeMap(antenas, mapp)

#drawAntinodesMap(copyMap, antinodes)

print(len(antinodes))