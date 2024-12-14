import re



file = open(__file__ + '\\..\\testInput.txt', 'r')
#file = open(__file__ + '\\..\\input.txt', 'r')

regions = []
inputMap = []
directions = [
    [-1, 0], [1, 0], [0, -1], [0, 1]
]


for i, line in enumerate(file.readlines()):
    line = line.removesuffix("/n")
    inputMap.append(list(line))
 
                



print(result) # 29388
