totalCards = int(input("Set count of cards"))
totalSum = 0
remaining_sum = 0
for card in range(1,totalCards+1):
    totalSum += card
for card in range(totalCards - 1):
    remaining_card = int(input("Set number of  card:"))
    remaining_sum += remaining_card
summ = totalSum - remaining_sum
print('The number of lost card is :',summ)