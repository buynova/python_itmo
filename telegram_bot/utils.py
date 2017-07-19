import telebot
import random


def generate_markup(*args):
    """Формирование клавиатуры с вариантами ответов"""
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    list_items = []
    for arg in args:
        list_items.append(arg)
    random.shuffle(list_items)

    for item in list_items:
        markup.add(item)
    markup.add('ВЫЙТИ')

    return markup
