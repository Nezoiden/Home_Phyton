# 1- Определить, присутствует ли в заданном списке строк, некоторое число


list_task1 = ['sdf', 'werwe', '2', 'rewq']
list_task1 = True in [n.isdigit() for n in list_task1]
print(list_task1)