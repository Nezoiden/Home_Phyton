import telebot
import random
from random import randint
import config
from telebot import types, TeleBot
from distutils.cmd import Command
import requests
import json

bot = telebot.TeleBot(config.TOKEN)

# @bot.message_handler(commands=['start'])
# def send_start(message):
# 	bot.send_message(message.chat.id, 'Приветствую тебя! Подробная информация в справке (/help) или в меню (/menu)')


contacts = {}
# API_URL='https://7012.deeppavlov.ai/model'

# contact = r'E:\Learning\GeekBrains\GIT\GB\Python\spravochnik\phone_directory.json'

def save(contacts): #метод сохранения как void в C#
    with open(contact, "a", encoding="utf-8") as fh: # "w" это метод write
        fh.write(json.dumps(contacts, ensure_ascii=False))  # fh это псевдоним
    print("Контакт сохранен")

def load(): #метод сохранения как void в C#
    with open(contact, "r", encoding="utf-8") as fh: # "w" это метод write
        contact=json.load(fh)
    print("Контакты загружены")

# API_TOKEN='5663390867:AAEYEU4JG3gc6bOoW9NsKGl-aLM_4Byy6iI'
# bot=telebot.TeleBot(API_TOKEN)  #создали экземпляр класса телебот с уникальными данными

# def start_message(message):
#     bot.send_message(message.chat.id, 'Телефонный справочник')
#     if contact not :
#         load()
#         bot.send_message(message.chat.id, "Справочник загружен")
#     except:
#         new_firstname()

@bot.message_handler(commands=['new_contact'])
#Фамилия, имя, номер, комментарий
def new_firstname(message):
    msg = bot.send_message(message.chat.id, "Введи фамилию:")
    bot.register_next_step_handler(msg, check_firstname)
# Phone_Book["name"] = test.correct_name()

def check_firstname(message):
    chat_id = message.chat.id
    text = message.text
    if text.isalpha():
        contacts["firstname"] = text
        new_name(message)
    if not text.isalpha():
        msg = bot.send_message(chat_id, "Введи фамилию")
        bot.register_next_step_handler(msg, check_firstname)

def new_name(message):
    msg = bot.send_message(message.chat.id, "Введи имя:")
    bot.register_next_step_handler(msg, check_name)

def check_name(message):
    chat_id = message.chat.id
    text = message.text
    if text.isalpha():
        contacts["name"] = text
        new_number(message)
    if not text.isalpha():
        msg = bot.send_message(chat_id, "Введи имя")
        bot.register_next_step_handler(msg, check_name)

def new_number(message):
    msg = bot.send_message(message.chat.id, "Введи номер телефона:")
    bot.register_next_step_handler(msg, check_number)

def check_number(message):
    chat_id = message.chat.id
    text = message.text
    if text.isdigit():
        contacts["number"] = text
        new_comment(message)
    if not text.isdigit():
        msg = bot.send_message(chat_id, "Введи номер телефона из ЦИФР")
        bot.register_next_step_handler(msg, check_number)

def new_comment(message):
    msg = bot.send_message(message.chat.id, "Введи комментарий:")
    bot.register_next_step_handler(msg, check_comment)

def check_comment(message):
    chat_id = message.chat.id
    text = message.text
    contacts["comment"] = text
    save(contacts)
    # new_name(message)


# def initial_step_1(message):
#     bot.send_message(message.chat.id, "Добро пожаловать в игру в конфеты")
#     msg = bot.send_message(message.chat.id, "Для начала определись, сколько всего будет конфет. Введите число.")
#     bot.register_next_step_handler(msg, check_candies)

# def initial_step_2(message):
#     msg = bot.send_message(message.chat.id, "Сейчас назови количество конфет, которое можно брать за ход. Введите число.")
#     bot.register_next_step_handler(msg, check_bot_can_take)

# def check_candies(message) -> str:
#     chat_id = message.chat.id
#     text = message.text
#     if text.isdigit() and text.isdigit() > 0:
#         candy_logic.total_candies = int(text)
#         bot.send_message(message.chat.id, f'Доступно {candy_logic.total_candies} конфет')
#         initial_step_2(message)
#     if not text.isdigit():
#         msg = bot.send_message(chat_id, "Введи ЦИФРАМИ (положительными, строго больше 0) количество конфет!")
#         bot.register_next_step_handler(msg, check_candies)


@bot.message_handler(commands=['all'])
def show_all(message):
    bot.send_message(message.chat.id, "Вот список фильмов")
    bot.send_message(message.chat.id, ", ".append(contacts))

# @bot.message_handler(commands=['wiki'])
# # def wiki(message):
# #     quest = message.text.split()[1:] #приняли запрос от пользователя и положили в переменную сплит и в массив
# #     qq=" ".append(quest)
# #     data = {'question_raw': [qq]} #формируем запрос
# #     try:  #если нашёл ответ на запрос
# #         res = requests.post(API_URL, json=data, verify=False).json() # посылаем запрос и  получаем обратоно
# #         bot.send_message(message.chat.id, res)
# #     except:   #если НЕ нашёл ответ на запрос
# #         bot.send_message(message.chat.id, "что-то  я ничего не нашёл :((")
# #     # bot.send_message(message.chat.id, ", ".append(contacts))




print('server started')


bot.polling(none_stop=True)
bot.infinity_polling()