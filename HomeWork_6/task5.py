# 5- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

list_1 = [2, 3, 4, 5, 6]  # [12, 15, 16]
size = int(len(list_1) / 2)
result = list(
    map(lambda x, y: x * y, list(reversed(list_1)), list_1[:-size]))
print(f'{list_1} -> {result}')