#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

rules = []
books = []
second = False

def findIndex(pages: list, number: int):
    try:
        return pages.index(number)
    except ValueError:
        return -1

for line in file.readlines():
    
    if line == "\n":
        second = True
        continue
    line = line.removesuffix("\n")
    
    if second:        
        books.append(list(map(int, line.split(","))))
    else:
        rules.append(list(map(int, line.split("|"))))

def correctOrder(pages):
    i = 0
    while i < len(rules):
        firstRuleIndex = findIndex(pages, rules[i][0])
        secondRuleIndex = findIndex(pages, rules[i][1])
        if  firstRuleIndex > secondRuleIndex and firstRuleIndex != -1 and secondRuleIndex != -1:
            temp = pages[firstRuleIndex]
            pages[firstRuleIndex] = pages[secondRuleIndex]
            pages[secondRuleIndex] = temp
            i = 0
        else:
            i += 1

    return pages



result = 0
correctedPages = []
for pages in books:
    isCorrect = True
    for rule in rules:
        firstRuleIndex = findIndex(pages, rule[0])
        secondRuleIndex = findIndex(pages, rule[1])
        if  firstRuleIndex > secondRuleIndex and firstRuleIndex != -1 and secondRuleIndex != -1:
            correctedPages.append(correctOrder(pages))            
            break

for cp in correctedPages:
    result += cp[int((len(cp) - 1 ) / 2)]

print(result)

    