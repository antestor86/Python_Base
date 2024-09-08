text = input("Add text: ")
first_sym = input("Add first word:")
second_sym = input("Add second word:")
first_sym_count = 0
second_sym_count = 0
for symbol in text:
    if symbol == first_sym:
        first_sym_count += 1
    if symbol == second_sym:
        second_sym_count += 1
print(first_sym,"count=",first_sym_count)
print(second_sym,"count=",second_sym_count)

