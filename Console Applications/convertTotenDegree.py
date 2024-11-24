def convert_to_tendegree(value):
    divider = 0
    while value > 10:
        value /= 10
        divider += 1
    result = f'x ={value}*10**{divider}'
    return result
a = convert_to_tendegree(16)
print(a)