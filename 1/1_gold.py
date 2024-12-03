import os

path = "\..\input.txt"

file = open(__file__ + path, 'r')
print(input)

left = list()
dict = {}

for line in file.readlines():
    print(line)
    if int(line) == 0:
        continue
    list = str(line).split('   ')
    
    left.append(list[0])
    if list[1] in dict:
          dict[list[1]] = dict[list[1]] + 1
    else:
        dict[list[1]] = 1

dist = 0
for i in range(len(left)):
    if left[i] in dict:
        dist += left[i] * dict[left[i]]



print(dist)