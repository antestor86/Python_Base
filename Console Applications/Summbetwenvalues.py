summ = 0
first_number = int(input("Set start"))
end_number = int(input("set end"))
for number in range(first_number,end_number+1):
    if first_number < end_number:
        summ += number

print(summ)