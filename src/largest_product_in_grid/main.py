data = []
answer = 0
with open('/Users/daniel/personal/ProjectEuler/src/largest_product_in_grid/data.txt') as file:
    line = file.readline()
    while line:
        row = [int(x) for x in line.split()]
        data.append(row)
        line = file.readline()
for i in range(len(data)):
    for j in range (len(data[i])):
        horizontal_product = data[i][j] * data[i][j+1] * data[i][j+2] * data[i][j+3] if j <= 16 else 0
        vertical_product = data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j] if i <= 16 else 0
        lr_diagonal_product = data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3] if i <= 16 and j <= 16 else 0
        rl_diagonal_product = (data[i][j] * data[i-1][j-1] * data[i-2][j-2] * data[i-3][j-3]) if i >= 3 and j <= 16 else 0
        curr_max = max(horizontal_product, vertical_product, rl_diagonal_product, lr_diagonal_product)
        if curr_max > answer:
            # print(answer, curr_max)
            answer = curr_max

print(answer)