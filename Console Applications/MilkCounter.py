full_milk = 0
for milk in range(0,20,2):
    ab_text = input("Enter a or b ")
    milk += 2
    if ab_text == "b":
        full_milk += milk
    elif ab_text == "a":
        continue

print(full_milk)



