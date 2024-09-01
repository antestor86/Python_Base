summ_of_positive_customers = 0
for sequence in range(0,11):
    customer = int(input("Write customer number:"))
    if customer > 0 and sequence % 2 !=0:
        summ_of_positive_customers += 1
print(summ_of_positive_customers)
