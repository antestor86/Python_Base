text = input("Write text ")
first_counter = 0
second_counter = 0
big_text = 0
main_text = ""
for item in text:
    first_counter += 1
    if item == " ":
        if first_counter > second_counter:
            second_counter = 0
        elif second_counter > first_counter:
            first_counter = 0
        second_counter = first_counter
        first_counter = 0

if first_counter > second_counter:
    big_text = first_counter - 1
else:
    big_text = second_counter - 1

print("The biggest word is ",big_text)
print(main_text)