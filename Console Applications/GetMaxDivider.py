def gcd(a,b):
    max = 0
    for item in range(1,b):
        if a % item == 0 and b % item == 0:
            max = item
        else:
            continue
    return max

a = gcd(3,9)
print(a)