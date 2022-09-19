# 2 - Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.
#   Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


listNumbers = list(map(int, input('Введите числа через пробел: ').split()))

def FindNonRepeatingNum(listNumbers):
    
    result = []
    print(listNumbers, end= ' -> ')
    for i in listNumbers:
        if i not in result:
            result.append(i) 
    print(result)

FindNonRepeatingNum(listNumbers)