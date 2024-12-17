import math
def calculate_dagerous_depth(max_level):
    save_depth = max_level**3 - math.pow(3*max_level,2) - 12*max_level + 10
    res = f'{save_depth}m'
    return res
calc = float(input("Add max depth: "))
a = calculate_dagerous_depth(calc)
print(a)
