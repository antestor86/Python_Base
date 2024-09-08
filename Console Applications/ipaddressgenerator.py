number = int(input('Set first number:'))
step = int(input("Set second number:"))
summ = 0
print('\nIP-Address:',end=' ')
for count in range(3):
    print(number,end='.')
    summ +=number
    number += step
print(summ)