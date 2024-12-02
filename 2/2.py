

#file = open(__file__ + '\\..\\testInput.txt', 'r')
file = open(__file__ + '\\..\\input.txt', 'r')

nums = list()
safe = 0


def difference(num1, num2):
    diff = abs(num1 - num2)
    if (diff > 0 and diff <= 3):
        return True
    return False


for line in file.readlines():
    numbers = list(map(int,(line.split(' '))))
    isUp = 0
    isDown = 0
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            print(numbers)
            safe += 1
            break
        if i == 0:
            if numbers[i] > numbers[i + 1]:
                isDown = True
                isUp = False
            else:
                isDown = False
                isUp = True
        
        if isUp == True and numbers[i] < numbers[i + 1] and difference(numbers[i + 1], numbers[i]):
            continue
        elif isDown == True and numbers[i] > numbers[i + 1] and difference(numbers[i + 1], numbers[i]):
            continue
        else:
            break
        
print(safe)

