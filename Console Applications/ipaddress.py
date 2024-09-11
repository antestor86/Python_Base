number = int(input('Set first number'))
step = int(input('Set step :'))
summ = 0
print("IP Address:",end=" ")
for count in range(3):
    print(number,end=".")
    summ +=number
    number += step
print(summ)
