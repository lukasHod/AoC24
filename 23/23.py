
#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')


def printDict(dictionary: dict):

    for key, val in dictionary.items():
        print(f"{key}: {val}")


connections = {}
sets = {}
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    f, s = line.split('-')

    if f not in connections:
        connections[f] = [s]
    else:
        connections[f].append(s)
    if s not in connections:
        connections[s] = [f]
    else:
        connections[s].append(f)


for key, values in connections.items():
    for i, iVal in enumerate(values):
        for j, jVal in enumerate(values):
            if i == j: continue
            if jVal in connections[iVal]:
                hasTStart = key[0:1] == 't' or iVal[0:1] == 't' or jVal[0:1] == 't'
                
                sortedSet = [key, iVal, jVal]
                sortedSet.sort()
                finalSet = (',').join(sortedSet)

                if finalSet not in sets and hasTStart:
                    sets[finalSet] = 1

print(len(sets))