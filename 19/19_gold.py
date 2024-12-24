#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

memoSet = {}

def solve(input, fragments, maxFragmentsSize: int, currentSize: int, currentNode: dict):
    if input == '':
        return 1

    if input in memoSet: return memoSet[input]

    subs = ''
    nodeValue = 0
    for i in range(maxFragmentsSize+1):
        if i == 0: continue
        if i > len(input): break

        subs = input[0:i]
        if subs in fragments:
            currentNode[subs] = {}
            result = solve(input[i:], fragments, maxFragmentsSize, currentSize + 1, currentNode[subs])
            if result >= 0:
                nodeValue += result

    
    if input not in memoSet:
        memoSet[input] = nodeValue    
    else:
        memoSet[input] += nodeValue
    return nodeValue


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

all = 0
for i, input in enumerate(inputs):
    tree = {}
    memoSet = {}
    result = solve(input, fragments, maxFragmentsSize, 0, tree)
    all += memoSet[input]

print(all)
