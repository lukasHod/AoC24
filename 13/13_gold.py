import re



file = open(__file__ + '\\..\\testInput.txt', 'r')
#file = open(__file__ + '\\..\\input.txt', 'r')

input = {}
num = 0
for i, line in enumerate(file.readlines()):
    if i % 4 == 3:
        num +=1
        continue
    if num not in input:
        input[num] = {}
    vals =  re.findall(r"[+-]?\d+", line)
    if i % 4 == 0:
        input[num]['A'] = {"x": int(vals[0]), 'y': int(vals[1])}
    if i % 4 == 1:
        input[num]['B'] = {"x": int(vals[0]), 'y': int(vals[1])}
    if i % 4 == 2:
        input[num]['P'] = {"x": int(vals[0]) + 10000000000000, 'y': int(vals[1]) + 10000000000000}
    
    
result = 0
for num in input:
    print(f'{num} {input[num]}')
    inp = input[num]
    cheapest = -1
    i = int(inp['P']['x'] / inp['B']['x'])
    while i >= 0:
        n = (inp['P']['x'] - i*inp['B']['x']) / inp['A']['x']
        if n == int(n) and int(n) >= 0:
            if n*inp['A']['x'] + i*inp['B']['x'] == inp['P']['x'] and n*inp['A']['y'] + i*inp['B']['y'] == inp['P']['y']:
                print(f"n: {n} m: {i}")
                cost = 3*int(n) + i
                if cheapest == -1 or cheapest > cost:
                    cheapest = cost
                    print(f"cheapest: {cheapest}")
        i -= 1
    if cheapest != -1:
        result += cheapest


print(result) # 29388
