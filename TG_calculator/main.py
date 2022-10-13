import check
import logger
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler


# Решил не переносить наш калькулятор, а попробовать разобраться и доделать вариант
# показанный Вами.




logging.basicConfig(filename='logger.log',
format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO )


RAZIONAL = 'Рациональные'
COMPLEX = 'Комплексные'
WAY, ENTER_FLOAT, ENTER_COMPLEX, OPERATION = range(4)

def start(update, _):
    
    reply_keyboard = [[RAZIONAL, COMPLEX]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
   
    update.message.reply_text(
        'Добро пожаловать в Калькулятор. Выберите, с какими числами вы будете работать?',
        reply_markup=markup_key,)

    return WAY

def choose_path_to_work(update, _):
    way = update.message.text
    if way == RAZIONAL:
        update.message.reply_text('Вы выбрали режим рациональных чисел')
        update.message.reply_text('Введите первое число: ')
        return ENTER_FLOAT
    elif way == COMPLEX:
        update.message.reply_text('Вы выбрали режим комплексных чисел чисел')
        update.message.reply_text('Введите первое число вида ...+ ...j : ')
        return ENTER_COMPLEX
    update.message.reply_text('Вы выбрали несуществующий режим')

def get_float_number(update, context):
    num = update.message.text
    if not check.check_realnumber(update, num):
        return ENTER_FLOAT
    
    update.message.reply_text(f'Вы ввели число {num}')
    which = 'num1' if 'num1' not in context.user_data else 'num2'
    context.user_data[which] = int(num)
    if 'num2' not in context.user_data:
        update.message.reply_text('Теперь введи второе число')
        return ENTER_FLOAT
    update.message.reply_text('Теперь введите операцию: +, -, * или /')
    return OPERATION

def get_complex_number(update, context):
    num = update.message.text
    if not check.check_complexnumber(update, num):
        return ENTER_COMPLEX
    update.message.reply_text(f'Вы ввели число {num}')
    which = 'num1' if 'num1' not in context.user_data else 'num2'
    context.user_data[which] = complex(num)
    if 'num2' not in context.user_data:
        update.message.reply_text('Теперь введи второе число')
        return ENTER_COMPLEX
    update.message.reply_text('Теперь введите операцию: +, -, * или /')
    return OPERATION

def get_operation(update, context):
    oper = update.message.text
    if not check.check_operation(update, oper):
        return OPERATION
    context.user_data['oper'] = oper
    num1 = context.user_data.get('num1')
    num2 = context.user_data.get('num2')
    expression = f'{num1} {oper} {num2}'
    update.message.reply_text(f'{expression} = {eval(expression)}')
    text_log = f"{num1} {oper} {num2} = "
    result = eval(expression)
    logger.log(text_log, result) 
    context.user_data.clear()
    return ConversationHandler.END


def cancel(update, _):
    user = update.message.from_user
    text_log = "Пользователь %s отменил разговор."
    logger.log(text_log, user) 
    update.message.reply_text(
        'До свидания!'
        ,
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END




     



   