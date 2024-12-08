from itertools import product


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
            for j in range(len(typeAntenas)):
                if i == j: continue

                posB = typeAntenas[j]
                vector = [(posB[0] - posA[0]) * -1, (posB[1] - posA[1]) * -1]
                antinodePos = [posA[0] + vector[0], posA[1] + vector[1]]
                if antinodePos[0] >= 0 and antinodePos[0] < len(map) and antinodePos[1] >= 0 and antinodePos[1] < len(map[0]):
                    pos = f"{antinodePos[0]}-{antinodePos[1]}"
                    if pos not in antinodes:
                        antinodes.append(pos)
    return antinodes


def createMaps():
    antenas = {}
    map = []
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
        map.append(row)

        i += 1

    return [map, antenas]

maps = createMaps()
map = maps[0]
antenas = maps[1]

antinodes:list = createAntinodeMap(antenas, map)
print(len(antinodes))


#printArray(map) # 538191549061
#print(antenas)
