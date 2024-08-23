#replace fluids in  the cups
# Option 1
orange_juise_cup = "Orange Juice "
water_cup = "water"
temporary_cup = ""

print("In the orange juice cup ",orange_juise_cup)
print("In the water cup is the  ",water_cup)

temporary_cup = orange_juise_cup
orange_juise_cup = water_cup
water_cup = temporary_cup

print("In the orange juice cup ",orange_juise_cup)
print("In the orange juice cup  ",water_cup)

#Option 2
orange_juise_cup = "Orange Juice"
water_cup = "Water"
temporary_cup = ""
print("In the orange juice cup ",orange_juise_cup)
print("In the water cup   ",water_cup)

orange_juise_cup,water_cup = water_cup,orange_juise_cup

print("In the orange juice cup ",orange_juise_cup)
print("In the water cup  ",water_cup)