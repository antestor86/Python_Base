a = int(input("Add first number:"))
b = int(input("Add second number:"))
c = int(input("Add thirdth number:"))
maximum = 0
if a > b:
    maximum = a
else:
    maximum = b

if c > maximum:
    maximum = c

print("Maximum number ",maximum)