import itertools

primes_below_number = 2000000
numbers = [v % 2 != 0 for v in xrange(primes_below_number)]
numbers[0] = False
numbers[1] = False
numbers[2] = True

number = 3

while number < primes_below_number:
    n = number * 3  # We already excluded even numbers
    while n < primes_below_number:
        numbers[n] = False
        n += number
    number += 1
    while number < primes_below_number and not numbers[number]:
        number += 1

sum_of_numbers = sum(itertools.imap(lambda index_n: index_n[1] and index_n[0] or 0, enumerate(numbers)))

print(sum_of_numbers)