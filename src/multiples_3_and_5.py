multiples = {3}

for i in range(5, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.add(i)

print(sum(multiples))