# Найти расстояние между двумя точками пространства(числа вводятся через пробел)


import math

numbers = input("Введите координиты через пробел:")
list_1 = [float(n) for n in list(numbers.replace(" ", ""))]
sq = lambda x2, x1: (x2-x1)**2
print(round(math.sqrt((sq(list_1[2], list_1[0]) + sq(list_1[3], list_1[1]))), 2))