"""
 Реализуйте в боте команду /wordcount которая считает слова в присланной фразе. 
 Например на запрос /wordcount Привет как дела бот должен ответить: 3 слова. 
 
 Не забудьте:
    Добавить проверки на пустую строку
    Как можно обмануть бота, какие еще проверки нужны?
"""

import datetime, re
import ephem
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update,context):
  logging.info('Вызван /start')
  update.message.reply_text(
    'Привет, пользователь! Ты вызвал команду /start.\n'
    'Чтобы посчитать слова в присланной фразе наберите команду /wordcount <вставьте фразу>.\n'
    'Доступные планеты: Марс, Венера, Юпитер.'
  )

def wordcount(update, context):
    user_text = update.message.text
    symbols = '!"№;%:?*()@#$^&)-_+=[]{}<>,./|\\\''
    print(user_text)

    for char in symbols:
        user_text = user_text.replace(char, '')
    
    print(user_text)

    temp = re.findall(r'\d+', user_text)
    numb_list_1 = list(map(int, temp))
    numb_list_2 = str(list(map(int, temp)))



    for numb in numb_list_2:
        user_text = user_text.replace(numb, ' ')
    
    
    print(numb_list_1)
    print(user_text)

    logging.info(context.args)
    word_list = user_text.split()
    if len(word_list) > 0 and len(numb_list_1) == 0:
        update.message.reply_text(f'{len(word_list)} слова')
    elif len(word_list) > 0 and len(numb_list_1) > 0:
            update.message.reply_text(f'{len(word_list)} слова и {len(numb_list_1)} числа')   
    elif len(word_list) == 0:   
        update.message.reply_text('Чтобы посчитать слова вставьте после команды /wordcount фразу')
    print(word_list)


def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
