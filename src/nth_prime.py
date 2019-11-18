def ifPrime(n):
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

n = 10001
count = 3

curr = 5

while (count < n):
    curr = curr + 2
    if (ifPrime(curr)):
        count = count + 1

print(curr)