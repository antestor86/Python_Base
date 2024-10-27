heigth = float(input("Ваш Рост : "))
weight = float(input("Ваш вес  : "))
bmi = round(weight/heigth**2,2)
print('Ваш индекс массы тела : ',bmi)

if bmi < 18.5:
    print("У вас недостатчная масса тела : ")
elif bmi < 25 :
    print('У вас нормальная масса тела: ')
elif bmi < 30:
    print("У вас избиточная масса тела: ")
else:
    print("У вас ожирение")