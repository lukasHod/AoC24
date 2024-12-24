import heapq
import copy

from collections import defaultdict



#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

memoSet = set()

def solve(input, fragments, maxFragmentsSize: int, currentSize: int, currentNode: dict):
    if input == '':
        return currentSize

    subs = ''
    minSize = -1
    for i in range(maxFragmentsSize+1):
        if i == 0: continue
        subs = input[0:i]

        if subs in fragments:
            currentNode[subs] = {}
            if input[i:] in memoSet: continue
            minSizeS = solve(input[i:], fragments, maxFragmentsSize, currentSize + 1, currentNode[subs])
            if minSizeS != False:
                return minSizeS
            else:
                memoSet.add(input[i:])
    
    if minSize == -1:
        return False
    return minSize

       
   # for i, val in enumerate(input):
   #     subs 

    #for i, val in enumerate(inputLen):


fragments: set
first = True
dictionaryList = []
sortedFragments = {}
inputs = []
maxFragmentsSize = 0
fragments = {'one'}
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    if line == '':
        first = False
        continue
    if first:
        dictionaryList = line.split(', ')
    else:
        inputs.append(line)

for dl in dictionaryList:
    if len(dl) > maxFragmentsSize:
        maxFragmentsSize = len(dl)
    fragments.add(dl)
fragments.remove('one')
print(fragments)

print(maxFragmentsSize)
#print(sortedFragments)
#print(inputs[0])
all = 0
for i, input in enumerate(inputs):
    print('--------------------------------')
    print(i)
    print(input)
    tree = {}
    memoSet = set()
    result = solve(input, fragments, maxFragmentsSize, 0, tree)
    if result != False:
        all += 1

print(all)