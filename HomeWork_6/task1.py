# 1- Определить, присутствует ли в заданном списке строк, некоторое число


list = ['sdf', 'werwe', '2', 'rewq']
list = True in [n.isdigit() for n in list]
if list == True:
    print(f'В списке присутствует некоторое число')
else: 
    print(f'В списке отсутствует некоторое число')
