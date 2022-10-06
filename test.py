# def quadr(x):
#     return x**2


# list = [(i, quadr(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8  15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# data = open('students.txt', 'r+', encoding = 'utf-8')
# for lines in data:
#     if '5' in lines:
#         data.write('\n'+ lines.upper())
    
#         print(lines)
# data.close()


# word = str(raw_input("Введите букву:\n"))
# num = str(5)

# search_seq = [num]
# search_idx = 0

# with open('text.txt', 'w', encoding='utf-8') as file:
#     data = file.readlines()
    
#     for line in data:
#         search_elem = search_seq[search_idx]
#         if search_elem in line:
#             data.('\n'+ line.upper())
#             search_idx += 1
#             if not search_idx < len(search_seq):
#                 break
 

 # Функция, принимающая текст и сдвиг для шифровки
# и записывающая зашифрованный текст в файл (если файла нет, она его создает - режим w+)
# def encryptor(text, shift):
#     encrypted_text = ''
#     with open('encrypted_message.txt', 'w+', encoding='utf-8') as encrypted_message:
#         for letter in text:
#             encrypted_letter = chr(ord(letter) + shift)
#             encrypted_text += encrypted_letter
#         encrypted_message.write(encrypted_text)


# # Функция, принимающая файл с защифрованным текстом и сдвиг для дешифровки
# # и записывающая дешифрованный текст в новый файл (если файла нет, она его создает - режим w+)
# def decryptor(file, shift):
#     decrypted_text = ''
#     with open('decrypted_message.txt', 'w+', encoding='utf-8') as decrypted_message:
#         with open(file, 'r', encoding='utf-8') as encrypted_message:
#             for line in encrypted_message:
#                 for letter in line:
#                     decrypted_letter = chr(ord(letter) - shift)
#                     decrypted_text += decrypted_letter
#         decrypted_message.write(decrypted_text)




# encryptor('привет', -2)
# decryptor('encrypted_message.txt', -2)

from random import randint
from sys import exit




def check_win(m, n, k):
    if m == 1 and n == 0 and k == 0:
        return 'Выиграл Ботяня!'
    elif m == 0 and n == 0 and k == 0:
        return 'Вы выиграли!'
    elif m == 1 and n == 0 and k == 1:
        return 'Выиграл игрок 2!'
    elif m == 0 and n == 0 and k == 1:
        return 'Выиграл игрок 1!'
    return None  



def Game_mode(a):
    if a == 1: Bot_game(candy)
    elif a == 2: Player_1(candy)
    elif a == 3: Player_2(candy)
    else: return Menu()

def Menu():
    global candy
    candy = int(input('Введите колличество конфет: '))
    print()
    print(f'На столе лежит {candy} конфет(а). За один ход можно взять от 1 до 28 конфет.\nВыигрывает тот, кто забрал последнюю конфету.')
    print()
    game = int(input("Выберите против кого будете играть:\n1 - Бот\n2 - Игрок\nВаш Выбор: "))
    if game == 1: Game_mode(1)
        
    else: 
        print("Судьба определила кто будет ходить первым:")
        game = Game_mode(randint(2,3))
        
    

def Bot_game(n):
    k = 0
    j = 0
    
    while n > 0:
        if n >= 28:
            
            count_user = int(input('Сколько хотите взять конфет? (от 1 до 28): '))
            
                        
            while count_user < 1:
                count_user = int(input("Бери больше, не стесняйся!\nВозьми от 1 до 28 : ")) 
            while count_user > 28:
                count_user = int(input("А попа не слипнется? Не жадничай!\nВозьми от 1 до 28 : ")) 
        else: 
            count_user = int(input(f'Сколько хотите взять конфет? от 1 до {n}): '))
            while count_user < 1 or count_user > n:
                count_user = int(input(f'Похоже у Вас дрогнула рука...\n спокойно, не спеша введите цифру от 1 до {n} : '))
        
        n = n - count_user
        print(f"Вы съели: {count_user} конфет\nОсталось {n} конфет")
        result = check_win(j, n, k)
        if result:
            print(result)
            exit()
        j = 1
        count_bot = n % 29
        n = n - count_bot
        print(f'Ботяня взял: {count_bot} конфет\nОсталось {n} конфет.')
        result = check_win(j, n, k)
        j = 0
        if result:
            print(result)
            exit

def Player_1(n):
    k = 1
    j = 0
    

    while n > 0:
        print('Ход игрока 1!')
        if n >= 28:
            
            count_user = int(input('Сколько хотите взять конфет? (от 1 до 28): '))
                                    
            while count_user < 1:
                count_user = int(input("Бери больше, не стесняйся!\nВозьми от 1 до 28 : ")) 
            while count_user > 28:
                count_user = int(input("А попа не слипнется? Не жадничай!\nВозьми от 1 до 28 : ")) 
        else: 
            count_user = int(input(f'Сколько хотите взять конфет? от 1 до {n}): '))
            while count_user < 1 or count_user > n:
                count_user = int(input(f'Похоже у Вас дрогнула рука...\n спокойно, не спеша введите цифру от 1 до {n} : '))
        
        n = n - count_user
        print(f"Игрок 1 съел {count_user} конфет\nОсталось {n} конфет")
        result = check_win(j, n, k)
        if result:
            print(result)
            exit()
        j = 1
        Player_2(n)

def Player_2(n):
    k = 1
    j = 1
    

    while n > 0:
        print('Ход игрока 2!')
        if n >= 28:
            
            count_user = int(input('Сколько хотите взять конфет? (от 1 до 28): '))
                                    
            while count_user < 1:
                count_user = int(input("Бери больше, не стесняйся!\nВозьми от 1 до 28 : ")) 
            while count_user > 28:
                count_user = int(input("А попа не слипнется? Не жадничай!\nВозьми от 1 до 28 : ")) 
        else: 
            count_user = int(input(f'Сколько хотите взять конфет? от 1 до {n}): '))
            while count_user < 1 or count_user > n:
                count_user = int(input(f'Похоже у Вас дрогнула рука...\n спокойно, не спеша введите цифру от 1 до {n} : '))
        
        n = n - count_user
        print(f"Игрок 2 съел {count_user} конфет\nОсталось {n} конфет")
        result = check_win(j, n, k)
        if result:
            print(result)
            exit()
        j = 0           
        Player_1(n)
    
Menu()




