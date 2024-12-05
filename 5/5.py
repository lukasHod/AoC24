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

result = 0

for pages in books:
    isCorrect = True
    for rule in rules:
        firstRuleIndex = findIndex(pages, rule[0])
        secondRuleIndex = findIndex(pages, rule[1])
        if  firstRuleIndex > secondRuleIndex and firstRuleIndex != -1 and secondRuleIndex != -1:
            isCorrect = False
            break

    if isCorrect:
        result += pages[int((len(pages) - 1 ) / 2)]

print(result)

    