import re

#testInput: xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')
result = 0
fileText = ''
for line in file.readlines():
    fileText += line

all = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", fileText) 
isEnabled = True
for inst in all:
    if str(inst).startswith("mul") and isEnabled:
        instNums = re.findall(r"\d+", inst)
        result += int(instNums[0]) * int(instNums[1])
    elif str(inst).startswith("don"):
        isEnabled = False
    elif str(inst).startswith("do("):
        isEnabled = True

print(result)