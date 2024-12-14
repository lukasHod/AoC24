import copy



#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')


def printArray(listMap):
    for m in listMap:
        print(m)

rounds = 75
stones = []
def evolve():
    lastIndex = len(stones)
    for index, value in enumerate(stones):
        if index == lastIndex: break
        if value == 0:
            stones[index] = 1
            continue
        if len(str(value)) % 2 == 0:
            midpoint = len(str(value)) // 2
            v1 = int(str(value)[:midpoint])
            v2 = int(str(value)[midpoint:])
            stones[index] = v1
            stones.append(v2)
            continue
        stones[index] = value * 2024

for i, line in enumerate(file.readlines()):
    stones = list(map(int, line.removesuffix("\n").split(" ")))

    for round in range(rounds):
        evolve()
        print(f"round: {round} len: {len(stones)}")
    
print(len(stones))
