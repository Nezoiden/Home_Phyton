# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


N = 5
list_1 = list(map(lambda x: (-3) ** x, range(N)))
print(f'Для N = {N}: {list_1}')