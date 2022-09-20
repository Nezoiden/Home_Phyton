# 3 - В файле, содержащем фамилии студентов и их оценки, 
# изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

textFile = 'students.txt'

def OverwritingFile(data):
    with open(data, 'r', encoding='utf-8') as file:
        data_file = file.read().split('\n')

    for i in range(len(data_file)):
        index_str = data_file[i].split(' ')
        if len(index_str) < 3:
            continue
        rating = int(index_str[2])
        if rating > 4:

            data_file[i] = data_file[i].upper() 
            # data_file[i] = data_file[i].lower()

    with open(data, 'w', encoding='utf-8') as file:
            print(*data_file, file=file, sep="\n")

OverwritingFile(textFile)