from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
import random
from config import TOKEN


bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher



def start(update, context):
    context.bot.send_message(update.effective_chat.id, """===================Игра в конфеты!=====================
    На столе лежит N конфет (задается в начале игры).
    Играют два игрока делая ход друг после друга.
    Первый ход определяется жеребьёвкой. 
    За один ход можно забрать не более чем K конфет
    (задается в начале игры). 
    Тот, кто берет последнюю конфету - проиграл.     
    ===Для начала игры введите нажмите -> /game===""")
   
def game(update, context):
    context.bot.send_message(update.effective_chat.id, """Выберите с кем будите играть:
    1) Игра с ботом          --> /BOT
    2) Игра с человеком --> /PLAYER  """)  
    global step
    step = 0                                                      



def game_by_steps(update, context):
    global step, g_mode, candies_at_once, total_candies, player, take_candies
    if step == 0:
        g_mode = update.message.text
        if g_mode == '/BOT':
            context.bot.send_message(update.effective_chat.id, "Выбрана игра с ботом")
            context.bot.send_message(update.effective_chat.id, "Введите сколько максимально конфет можно взять за ход (любое число больше нуля)")
            step += 1
        elif g_mode == '/PLAYER':
            context.bot.send_message(update.effective_chat.id, "Выбрана игра с человеком")
            context.bot.send_message(update.effective_chat.id, "Введите сколько максимально конфет можно взять за ход (любое число больше нуля)")
            step += 1
        else:
            context.bot.send_message(update.effective_chat.id, 'Вы ввели некорректные данные. Попробуйте еще раз')
    elif step == 1:
        try:
            candies_at_once = int(update.message.text)
            if candies_at_once > 0:
                context.bot.send_message(update.effective_chat.id, f'Введите общее количество конфет (больше {candies_at_once})')
                step += 1
            else:
                context.bot.send_message(update.effective_chat.id, 'Число должно быть больше нуля. Попробуйте еще раз')
        except:
            context.bot.send_message(update.effective_chat.id, 'Вы ввели не число. Попробуйте еще раз')
    elif g_mode == '/BOT' and step == 2:
        try:
            total_candies = int(update.message.text)
            if total_candies > candies_at_once:
                context.bot.send_message(update.effective_chat.id, f'Первым ходит человек')
                context.bot.send_message(update.effective_chat.id, f'Введите количество конфет(не более {candies_at_once})')
                player = 1
                step += 1
            else:
                context.bot.send_message(update.effective_chat.id, f'Число должно быть больше {candies_at_once}. Попробуйте еще раз')
        except:
            context.bot.send_message(update.effective_chat.id, 'Вы ввели не число. Попробуйте еще раз') 
    elif g_mode == '/BOT' and step == 3:
        if total_candies > candies_at_once:  
            if player == 1:
                game_step(update, context)
                change_player()
                if 0 < take_candies <= candies_at_once:
                    return game_step_bot(update, context)
        elif 1 < total_candies <= candies_at_once: 
            candies_at_once = total_candies
            if player == 1:
                game_step(update, context)
                change_player()
                if 0 < take_candies <= candies_at_once:
                    return game_step_bot(update, context)
        else:
            if player == 1:
                context.bot.send_message(update.effective_chat.id, 'Выиграл бот')
            else:
                context.bot.send_message(update.effective_chat.id, 'Выиграл человек')
    elif g_mode == '/PLAYER' and step == 2:
        try:
            total_candies = int(update.message.text)
            if total_candies > candies_at_once:
                player = random.randint(1,2)
                context.bot.send_message(update.effective_chat.id, f'Путем жеребьевки первым ходит игрок {player}')
                context.bot.send_message(update.effective_chat.id, f'Введите количество конфет(не более {candies_at_once})')
                step += 1
                change_player()
            else:
                context.bot.send_message(update.effective_chat.id, f'Число должно быть больше {candies_at_once}. Попробуйте еще раз')
        except:
            context.bot.send_message(update.effective_chat.id, 'Вы ввели не число. Попробуйте еще раз')
    elif g_mode == '/PLAYER' and step == 3:
        if total_candies > candies_at_once:
            game_step(update, context)
            change_player()
        elif 1 < total_candies <= candies_at_once: 
            candies_at_once = total_candies
            game_step(update, context)
            change_player()
        else:
            context.bot.send_message(update.effective_chat.id, f'Выиграл игрок {player}')
            step += 1
    elif step == 4:
           context.bot.send_message(update.effective_chat.id, 'Игра окончена. Если хотите еще играть, введите /game')        

def change_player():
    global player
    if player == 1:
        player = 2
    else:
        player = 1


def game_step(update, context):
    global take_candies, total_candies, player, step, candies_at_once
    try:
        take_candies = int(update.message.text)
        if 0 < take_candies <= candies_at_once:
            total_candies = total_candies - take_candies
            if total_candies > 0:
                context.bot.send_message(update.effective_chat.id, f'Осталось конфет: {total_candies}')
                if g_mode == '/PLAYER':
                    context.bot.send_message(update.effective_chat.id, f'Теперь ходит игрок {player}')
                else:
                    context.bot.send_message(update.effective_chat.id, f'Теперь ходит бот')
            else:
                context.bot.send_message(update.effective_chat.id, f'Выиграл игрок {player}')
                step += 1
        else:
            context.bot.send_message(update.effective_chat.id, f'Можно взять не более {candies_at_once} конфет и не менее 1 конфеты')
    except:
        context.bot.send_message(update.effective_chat.id, 'Вы ввели не число. Попробуйте еще раз')

def game_step_bot(update, context):
    global take_candies, candies_at_once, total_candies, step 
    take_candies = (total_candies-1)%(candies_at_once+1)
    if take_candies > 0:
        total_candies = total_candies - take_candies
        context.bot.send_message(update.effective_chat.id, f'Бот взял конфет: {take_candies}')
        context.bot.send_message(update.effective_chat.id, f'Осталось конфет: {total_candies}')
        change_player()
        context.bot.send_message(update.effective_chat.id, f'Теперь ходит игрок {player}')
    else:
        context.bot.send_message(update.effective_chat.id, f'Выиграл человек')
        step += 1

      
def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Неизвестная команда. Проверьте правильность ввода')

def show_step(update, context):
    global step
    context.bot.send_message(update.effective_chat.id, step)

player_handler = CommandHandler('PLAYER', game_by_steps)
bot_handler = CommandHandler('BOT', game_by_steps)
start_handler = CommandHandler('start', start)
game_handler = CommandHandler('game', game)
step_handler = CommandHandler('step', show_step)
message_handler = MessageHandler(Filters.text, game_by_steps)
unknown_handler = MessageHandler(Filters.command, unknown)  

dispatcher.add_handler(player_handler)
dispatcher.add_handler(bot_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(game_handler)
dispatcher.add_handler(step_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


print('server started')
updater.start_polling()
updater.idle()