#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')


def printDict(dictionary: dict):

    for key, val in dictionary.items():
        print(f"{key}: {val}")

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def createCombinations(lst) -> list:
    combos = set()
    for i, iVal in enumerate(lst):
        for j, jVal in enumerate(lst):
            if j == i: continue
            connection = [iVal, jVal]
            connection.sort()

            sKey = f"{connection[0]}-{connection[1]}"
            combos.add(sKey)
    return combos


connections = {}
sortedConnections = {}
intersections = {}
sets = {}
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    f, s = line.split('-')
    sortConnection = [f, s]
    sortConnection.sort()
    
    first, second = sortConnection[0],sortConnection[1]
    sKey = f"{first}-{second}"
    sortedConnections[sKey] = 1

    if f not in connections:
        connections[f] = [s]
    else:
        connections[f].append(s)
    if s not in connections:
        connections[s] = [f]
    else:
        connections[s].append(f)

for value in sortedConnections:
    f,s = value.split('-')
    l1 = connections[f] + [f]
    l2 = connections[s] + [s]

    intersectionList = intersection(l1, l2)
    intersectionList.sort()
    sortedConnections[value] = intersectionList

sortedConnections = dict(sorted(sortedConnections.items(), key=lambda item: len(item[1]), reverse=True))


for key, values in sortedConnections.items():
    comboElements = values
    combos = list(createCombinations(comboElements))

    i = 0
    isTheSame = True
    while isTheSame:
        if combos[i] not in sortedConnections or sortedConnections[combos[i]] != values:
            isTheSame = False
        i += 1
        if i >= len(combos):
            break
    if isTheSame == True:
        print((',').join(values))
        exit()
    