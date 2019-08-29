number1=int(input('Set First value: '))
number2=int(input('Set Second value: '))
for i in range(number1,number2):
    for j in range(2,i):
        if i % 2 == 0:
            print(i)
            break



