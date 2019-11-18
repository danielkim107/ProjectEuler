answer = 0

def generateFibonacci(first, second, answer):
    next = first + second
    if next > 4000000:
        print(answer)
        return
    if next % 2 == 0:
        answer = answer + next
    generateFibonacci(second, next, answer)


first = 1
second = 1

generateFibonacci(first, second, answer)