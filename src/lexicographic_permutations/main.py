import math

numbers = [0,1,2,3,4,5,6,7,8,9]
target = 1000000
answer = ''
for i in range(len(numbers) - 1, 0, -1):
    temp = target
    index = 0
    while temp - math.factorial(i) > 0:
        temp -= math.factorial(i)
        index += 1
    answer += str(numbers[index])
    numbers.remove(numbers[index])
    target = temp
answer += str(numbers[0])
print(answer)