import os

path = "\..\input.txt"

file = open(__file__ + path, 'r')
print(input)

left = list()
right = list()

for line in file.readlines():
    list = str(line).split('   ')
    left.append(int(list[0]))
    right.append(int(list[1]))

left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += (abs(right[i] - left[i]))


print(dist)

