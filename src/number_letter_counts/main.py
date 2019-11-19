units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
special_tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

answer = 0

for i in range(1,1000):
    if i/100 >= 1:
        answer += len(units[int(i/100)]) + len('hundred')
        if i % 100 != 0:
            answer += len('and')
    if int(i/10) % 10 == 1:
        answer += len(special_tens[i % 10])
    else:
        answer += len(tens[int(i / 10) % 10]) + len(units[i % 10])

answer += len('onethousand')
print(answer)