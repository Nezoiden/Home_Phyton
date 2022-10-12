from main import *
from config import TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(         
        entry_points=[CommandHandler('start', start)],
        
        states={
            WAY: [MessageHandler(Filters.regex('^(Рациональные|Комплексные)$'), choose_path_to_work)],
            ENTER_FLOAT: [MessageHandler(Filters.text & ~Filters.command, get_float_number)],
            ENTER_COMPLEX: [MessageHandler(Filters.text & ~Filters.command, get_complex_number)],
            OPERATION: [MessageHandler(Filters.text & ~Filters.command, get_operation)],
        },
           fallbacks=[CommandHandler('cancel', cancel)],
    )
    
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()