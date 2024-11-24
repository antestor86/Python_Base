def maximum_of_two(value1,value2):
    maximum = 0
    if value1 > value2:
        maximum = value1
    else:
        maximum = value2
    return maximum
def maximum_of_three(value1,value2,value3):
    max = maximum_of_two(value1,value2)
    maximum = 0
    if max > value3:
        maximum = max
    else:
        maximum = value3
    return  maximum


a = int(input("Add first number:"))
b = int(input("Add second number:"))
c = int(input("Add thirdth number:"))
res = maximum_of_three(a,b,c)
print('The maximu number is: ',res)