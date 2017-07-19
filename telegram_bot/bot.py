import telebot
import random

import telegram_bot.utils as utils
import telegram_bot.config as conf
from telegram_bot.db_work import DataBase

bot = telebot.TeleBot(conf.token)
row = None
markup = None


@bot.message_handler(commands=['words'])
def translate_words(message):
    """Упражнение 'Перевод слов'"""
    global row, markup

    db = DataBase(conf.db_name)
    row = db.select_word(random.randint(1, 50))
    words = db.select_all_translates_except(row[0])
    db.close()

    random.shuffle(words)
    markup = utils.generate_markup(row[3], words[0][0], words[1][0], words[2][0])
    with open(row[6], 'rb') as audio:
        bot.send_audio(message.chat.id, audio, reply_markup=markup)
    bot.register_next_step_handler(message, process_answer_words)


def process_answer_words(message):
    """Обработка ответа на упражнение 'Перевод слов'"""
    global row, markup
    if message.text == row[3]:
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "Верно! Еще раз? /words", reply_markup=markup)
    elif message.text == 'ВЫЙТИ':
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, conf.help_msg, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Неверно :( Попробуй снова", reply_markup=markup)


@bot.message_handler(commands=['start', 'help'])
def show_help(message):
    """Показать справку"""
    global markup

    markup = telebot.types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, conf.help_msg, reply_markup=markup)


@bot.message_handler(commands=['spanish'])
def translate_to_spanish(message):
    """Перевод на испанский язык"""
    global markup

    markup = telebot.types.ForceReply(selective=False)
    bot.send_message(message.chat.id, 'Введите слово на русском языке:', reply_markup=markup)
    bot.register_next_step_handler(message, process_answer_spanish)


def process_answer_spanish(message):
    """Обработка запроса на перевод слова"""
    db = DataBase(conf.db_name)
    rus = message.text
    rus = rus.strip()
    spanish = db.select_spanish(rus.lower())
    db.close()

    if not spanish:
        bot.send_message(message.chat.id, 'Слово {} не найдено в словаре. /spanish'.format(rus))
    else:
        bot.send_message(message.chat.id, spanish[0])
        if spanish[1]:
            with open(spanish[1], 'rb') as audio:
                bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['add'])
def add_new_word(message):
    """Добавление нового слова в словарь"""
    global markup

    markup = telebot.types.ForceReply(selective=False)
    bot.send_message(message.chat.id, 'Введите новое слово и его перевод через пробел:', reply_markup=markup)
    bot.register_next_step_handler(message, process_answer_add)


def process_answer_add(message):
    """Обработка запроса на добавление слова в словарь"""
    db = DataBase(conf.db_name)

    text = message.text.strip()
    esp, rus = text.split(' ')
    res = db.select_spanish(rus.lower())

    if res:
        bot.send_message(message.chat.id, 'Это слово уже есть в словаре!')
    else:
        db.add_new_word(esp.lower(), rus.lower())
        bot.send_message(message.chat.id, 'Слово добавлено!')

    db.close()


if __name__ == "__main__":
    bot.polling(none_stop=True)
