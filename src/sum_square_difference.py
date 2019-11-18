first = 0
second = 0

for i in range(1, 101):
    first += i*i
    second += i

second = second * second

print(first - second)