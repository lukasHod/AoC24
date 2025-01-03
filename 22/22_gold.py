
#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

allSequences = {}

def evolve(number):
    seqs = {}
    lastNum = int(str(number)[-1])
    changes = []
    for i in range(2000):
        r = number * 64
        xor = r ^ number
        mod = int(xor % 16777216)
        divS = int(mod / 32)
        mixD = divS ^ mod
        rM = mixD * 2048
        mixM = rM ^ mixD
        result = mixM % 16777216
        lastNumRes = int(str(result)[-1])
        
        change = lastNumRes - lastNum
        #print(f'lastNum: {lastNum} lastNumRes: {lastNumRes} change: {change}')
        changes.append(change)
        number = result
        lastNum = lastNumRes

        
        lastFours = changes[-4:]
        if len(lastFours) < 4:
            continue
        seq = ('').join(map(str, lastFours))
        if seq not in allSequences:
            allSequences[seq] = lastNumRes
            seqs[seq] = 1
        else:
            #store value for only first occurence TODO
            if seq not in seqs:
                seqs[seq] = 1
                allSequences[seq] += lastNumRes


result = 0
inputs = []
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    #print(line)
    evolve(int(line))

allSequences = dict(sorted(allSequences.items(), key=lambda item: item[1], reverse=True))

firstKey, firstValue = next(iter(allSequences.items()))
print(firstValue)

