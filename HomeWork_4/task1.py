# 1 - Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

n = int(input('Введите натуральное число: '))


def FindNumberMultiplier(n):
    multiplier = []
    a = 2
    m = n 
    while a * a <= n:
                if n % a == 0:
                    multiplier.append(a)
                    n//=a
                else:
                    a += 1
    multiplier.append(n) 

    print(f'N = {m} -> {multiplier}') 

FindNumberMultiplier(n)
