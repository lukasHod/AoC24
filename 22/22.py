
#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

def evolve(number):
    for i in range(2000):
        r = number * 64
        xor = r ^ number
        mod = int(xor % 16777216)
        divS = int(mod / 32)
        mixD = divS ^ mod
        rM = mixD * 2048
        mixM = rM ^ mixD
        result = mixM % 16777216
        number = result
    return number

result = 0
inputs = []
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    r = evolve(int(line))
    result += r

print(result)
