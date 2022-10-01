# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
#  Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#   За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
#    Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

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