answer = 0
for i in range(100,1000):
    for j in range(i,1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > answer:
                answer = product
print(answer)