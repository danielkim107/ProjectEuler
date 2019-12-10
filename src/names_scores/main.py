import os
import re

def orderFile(filename):
    file = open(filename, 'r')
    names = file.readline().split(',')
    for i in range(len(names)):
        names[i] = re.sub(r'\W+', '', names[i])
    names.sort()
    file.close()
    return names

alphabet_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 
'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

answer = 0

filename = os.getcwd() + '/test.txt'
names_list = orderFile(filename)


for i in range(len(names_list)):
    temp = 0
    for char in names_list[i]:
        temp += alphabet_map[char]
    answer += temp * (i + 1)

print(answer)