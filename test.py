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

# import telebot
# from telebot import types

# bot = telebot.TeleBot("5423669284:AAG1lXJhdCtJULEEhB7-54PpPDa7ghPxhz0")

# value = ""
# old_value = ""

# keyboard = telebot.types.InlineKeyboardMarkup()
# keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
#                 telebot.types.InlineKeyboardButton("C", callback_data="C"),
#                 telebot.types.InlineKeyboardButton("<=", callback_data="<="),
#                 telebot.types.InlineKeyboardButton("/", callback_data="/") )

# keyboard.row(   telebot.types.InlineKeyboardButton("7", callback_data="7"),
#                 telebot.types.InlineKeyboardButton("8", callback_data="8"),
#                 telebot.types.InlineKeyboardButton("9", callback_data="9"),
#                 telebot.types.InlineKeyboardButton("*", callback_data="*") )

# keyboard.row(   telebot.types.InlineKeyboardButton("4", callback_data="4"),
#                 telebot.types.InlineKeyboardButton("5", callback_data="5"),
#                 telebot.types.InlineKeyboardButton("6", callback_data="6"),
#                 telebot.types.InlineKeyboardButton("-", callback_data="-") )

# keyboard.row(   telebot.types.InlineKeyboardButton("1", callback_data="1"),
#                 telebot.types.InlineKeyboardButton("2", callback_data="2"),
#                 telebot.types.InlineKeyboardButton("3", callback_data="3"),
#                 telebot.types.InlineKeyboardButton("+", callback_data="+") )

# keyboard.row(   telebot.types.InlineKeyboardButton(" ", callback_data="no"),
#                 telebot.types.InlineKeyboardButton("0", callback_data="0"),
#                 telebot.types.InlineKeyboardButton(",", callback_data="."),
#                 telebot.types.InlineKeyboardButton("=", callback_data="=") )

# @bot.message_handler(commands = ["start", "calculater"] )
# def getmessage(message):
#     global value
#     if value == "":
#         bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
#     else:
#         bot.send_message(message.from_user.id, value, reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_func(query):
#     global value, old_value
#     data = query.data

#     if data == "no" :
#         pass
#     elif data == "C" :
#         value = ""
#     elif data == "=" :
#         try:
#             value = str(eval(value))
#         except:
#             value = "Ошибка!"
#     else:
#         value += data

#     if value != old_value:
#         if value == "":
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="0", reply_markup=keyboard)
#         else:
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)

#     old_value = value
#     if value == "Ошибка!": value = ""

# bot.polling(none_stop=False, interval=0)