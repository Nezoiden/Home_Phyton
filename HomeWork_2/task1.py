# 1 - Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

number = float(input('Введите дробное число: '))

def sum_number(num):
    if num < 0:
        num = num * -1
    str_num = str(num)
    str_num = str_num.replace('.', '')
    lst_str = list(str_num)
    lst_num = map(int, lst_str)
    s = sum(lst_num)
    print(f'{number} -> {s}')


sum_number(number)
