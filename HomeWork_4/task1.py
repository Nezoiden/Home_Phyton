# 1 - Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

number = int(input('Введите натуральное число: '))


def FindnumberMultiplier(number):
    multiplier = []
    a = 2
    m = number
    while number > 1:
        if number % a == 0:
            multiplier.append(a)
            while number % a == 0:
                number /= a
        else:
            a += 1
   

    print(f'N = {m} -> {multiplier}')


FindnumberMultiplier(number)
