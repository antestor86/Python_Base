import random
def makeRandomValue():
    result = random.randint(5,10)
    result /= random.randint(2,3)
    if result > 5 and result < 10:
        return round(result,2)
    else:
        result +=5
        return round(result,2)

list_range = 20

first_command = [makeRandomValue() for _ in range(list_range)]
second_command = [makeRandomValue()for _ in range(list_range)]

winners = []
for item in range(list_range):
    if first_command[item]>second_command[item]:
        winners.append(first_command[item])
    else:
        winners.append(second_command[item])

print(winners)


