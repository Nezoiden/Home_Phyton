# 3-Создайте два списка — один с названиями языков программирования,
#  другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
#  состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: 
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
#  то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
#  Порядковые номера смотрите в этой таблице, в третьем столбце: 
#  https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе
#  с преобразованным списком



list1 = ['Python', 'C#', 'C++']
list2 = list(range(1, len(list1)+1))
list3 = []
print(list2)
for i in range(len(list1)):
    list3.append(tuple([list2[i], list1[i]]))
print(list3)

for  index_lis in range(len(list3)):
    sum = 0
    elem = list3[index_lis]
    for index_tumpl in range(len(elem[1])):
        sum += ord((elem[1])[index_tumpl])
    
    
    if sum%(elem[0]) == 0:
        list3[index_lis] = tuple([sum, list1[index_lis]])
       
    else:
        list3[index_lis] = ''
print(list3)
