
def reverse(value):
    c = ''
    d = ''
    while value >= 1:
        c += str(value % 10)
        if value == 0:
            continue
        else:
            value = value // 10
    print(c)

def reverceInt(value):
    res = ''
    counter = 0
    for item in value:
        if item == "0":
            continue
        else:
            res += item
            counter += 1

# Последнюю цифру первого числа переносим во второе
    digit = int(res) % 10
    res2 = digit
# Избавляемся от последней цифры первого числа
    res = int(res) // 10
    while res > 0:
       # находим остаток - последнюю цифру
        digit = res % 10
       # делим нацело - удаляем последнюю цифру
        res = res // 10
       # увеличиваем разрядность второго числа
        res2 = res2 *10
       # добавляем очередную цифру
        res2 = res2 + digit
    print("Program Is Finished ! ",res2)


value = input("Value: ")
reverceInt(value)