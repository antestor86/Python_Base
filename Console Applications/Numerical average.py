start = int(input("start value:"))
end = int(input("end_value:"))
n = int(input("count :"))
summ = 0
for num in range(start,end):
    if num % n == 0:
       print("number ", num)
       summ+=num
artihmetic_mean = summ/n
print(artihmetic_mean)