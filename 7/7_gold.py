from itertools import product


#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

correct = 0

operators = ['+', '*', '|']
combinations = {}

def generateCombinations(input_list, length):
    combos = [list(combination) for combination in product(input_list, repeat=length)]
    if length not in combinations:
        combinations[length] = combos
    return combos


def resolve(result: int, numbers: list):
    combos = combinations[len(numbers)-1]

    for combo in combos:
        eq = str(numbers[0])
        for i in range(len(numbers)):
            if i < len(numbers)-1:
                if combo[i] == '|':
                    eq += str(numbers[i+1])
                else:
                    eq += str(combo[i]) + str(numbers[i+1])
                eq = str(eval(eq))

        res = int(eval(eq))
        if res == result:
            return result
    return False


for line in file.readlines():
    line = line.removesuffix("\n")
    instructions = line.split(": ")
    result = int(instructions[0])
    numbers = list(map(int,instructions[1].split(" ")))
    
    if len(numbers)-1 not in combinations:
        generateCombinations(operators, len(numbers) - 1)
    
    res = resolve(result, numbers)
    if res:
        correct += res

print(correct) # 34612812972206
