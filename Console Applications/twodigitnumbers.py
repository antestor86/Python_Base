#Write a program that finds and outputs all two-digit numbers
# that are equal to three times the product of their digits.
# These include, for example, 15 and 24.

first_value = int(input("Add First Value:"))
second_value = int(input("Add second Value:"))
for val in range(first_value,second_value):
    first_item = val // 10
    second_item = val % 10
    if (first_item * second_item)*3 == val:
        print(val)
