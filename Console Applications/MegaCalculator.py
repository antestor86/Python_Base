import math

# Получаем число от пользователя
number = float(input('Введите вещественное число: '))

# Применяем функции из модуля math
print('Округление вниз:', math.floor(number))
print('Округление вверх:', math.ceil(number))
print('Модуль числа:', math.fabs(number))
print('Квадратный корень:', math.sqrt(number))
print('Экспонента в степени числа:', math.exp(number))
print('Натуральный логарифм:', math.log(number))
print('Логарифм по основанию 2:', math.log2(number))
print('Логарифм по основанию 10:', math.log10(number))
print('Синус числа:', math.sin(number))
print('Косинус числа:', math.cos(number))

# Если число натуральное, вычисляем факториал
if number > 0 and number.is_integer():
    print('Факториал числа:', math.factorial(int(number)))
else:
    print('Факториал не вычисляется для данного числа.')

