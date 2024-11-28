def reverce_values(value1):
    output = ''
    for item in value1:
        output += str(int(value1) % 10)
        value1 = int(value1) // 10
    return output

def summ_of_reverce(value1,value2):
    output_1 = reverce_values(value1)
    output_2 = reverce_values(value2)
    summ = str(int(output_1) + int(output_2))
    reverce_summ = reverce_values(summ)
    return str(reverce_summ)

a = input("add first Value: ")
b = input("add second value: ")
res = summ_of_reverce(a,b)
print(res)


