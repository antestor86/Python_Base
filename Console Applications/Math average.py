a = int(input('Add first value:'))
b = int(input('Add second value:'))
average = 0
counter = 0
for number in range(a,b+1):
    if number % 3 == 0:
        average += number
        counter += 1
average = average/counter
print('Average:',average)