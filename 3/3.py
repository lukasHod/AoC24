
import re

#testInput: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')
result = 0
for line in file.readlines():
    all = re.findall(r"mul\(\d+,\d+\)", line) 
    for inst in all:
        instNums = re.findall(r"\d+", inst)
        result += int(instNums[0]) * int(instNums[1])

print(result)