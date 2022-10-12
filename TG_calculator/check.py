
def check_realnumber(update, text):
        try:
            num = float(text)
            return num
        except ValueError:
            update.message.reply_text('Промахнулись! Введите число: ')

def check_complexnumber(update, text):
    text = update.message.text
    try:
        num = complex(text)
        return num
    except ValueError:
        update.message.reply_text('Не верно введено комплексное число! Введите заново: ')

def check_operation(update, oper):
    oper_list = ['+', '-', '*', '/']
    if oper in oper_list:    
        return oper
       
    update.message.reply_text('Неверная операция! Введите что-то из этого: +, -, *, /')


