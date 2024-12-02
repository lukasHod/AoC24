

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

nums = list()
safe = 0


def difference(num1, num2):
    diff = abs(num1 - num2)
    if (diff > 0 and diff <= 3):
        return True
    return False

def checkLevels(numbers: list):
    isUp = numbers[0] < numbers[1]
    isDown = numbers[0] > numbers[1]

    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            return True

        if ((isUp == True and numbers[i] < numbers[i + 1]) or (isDown == True and numbers[i] > numbers[i + 1])) and difference(numbers[i + 1], numbers[i]):
            continue
        else:
            return False

    return False    
        

for line in file.readlines():
    numbers = list(map(int,(line.split(' '))))
    if checkLevels(numbers):
        safe += 1
        continue
    for i in range(len(numbers)):
        copyNum = numbers.copy()
        del copyNum[i]
        if checkLevels(copyNum):
            safe +=1
            break       
print(safe)

# < 659