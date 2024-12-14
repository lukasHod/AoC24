import copy



#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

class Stone:
    def __init__(self, value):
        self.v = value

    def getValue(self):
        return self.v
    
    def setValue(self, value):
        self.v = value

    def __str__(self) -> str:
        return f"value: {self.v}"



def printArray(listMap):
    for m in listMap:
        print(m)

stones = []
rounds = 25

def evolve(stones: list):
    evolvedStones = []

    for i, stone in enumerate(stones):
        value = stone.getValue()
        if value == 0:
            stone.setValue(1)
            evolvedStones.append(stone)
            continue
        if len(str(value)) % 2 == 0:
            midpoint = len(str(value)) // 2  # Find the midpoint
            v1 = int(str(value)[:midpoint])  # Slice the first half
            v2 = int(str(value)[midpoint:])  # Slice the second half
            stone.setValue(v1)
            s2 = Stone(v2)
            evolvedStones.append(stone)
            evolvedStones.append(s2)
            continue

        stone.setValue(value * 2024)
        evolvedStones.append(stone)
    return evolvedStones


for i, line in enumerate(file.readlines()):
    stoneLine = list(map(int, line.removesuffix("\n").split(' ')))
    for s in stoneLine:
        stone = Stone(int(s))
        stones.append(stone)
    
    for round in range(rounds):
        print(round)
        stones = evolve(stones)
    
print(len(stones))
