text = input("Write text ")
part_one = ""
part_two = ""
counter = 0
for item in text:
    counter += 1
    if counter % 2 != 0:
        part_one += item
    else:
        part_two = item + part_two

part_one = part_one + part_two
print(part_one)


