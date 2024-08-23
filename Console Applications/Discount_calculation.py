cource_price = 75000
your_wallet = int(input("Set how many money have you?"))
if your_wallet >= cource_price:
    your_wallet -= cource_price
    if your_wallet < 5000:
        your_wallet += 1000
        print("you have discount!!")
    print("Cource Succesfully bued!!!  ")
else:
    print("Nor enugh balance ")
print("Your balance>>",your_wallet)
print("Have nice day")