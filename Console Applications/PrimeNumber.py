number = int(input("Enter Number:"))
isPrime = True
for divider in range(2,number):
    if divider % number == 0:
        isPrime == False
        break
if isPrime:
    print('The number is prime')
else:
    print("The number is composite")