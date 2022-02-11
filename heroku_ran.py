from collections import Counter
import telebot
from utils import *
from token import *

import os
PORT = int(os.environ.get('PORT', 5000))




bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, rules)


f = open('countdown.txt', 'r')
dictionary = set(f.read().split('\n'))
f.close()

current_letters = None


def process_message(m):
    txt = m.text.strip()
    txt = txt.split(' ', 1)[1]
    return txt


@bot.message_handler(commands=["буквы"])
def start(m):
    global current_letters
    try:
        txt = process_message(m)
        nums = txt.split()
        if len(nums) == 2:
            v, c = map(int, nums)
            s = 0
        elif len(nums) == 3:
            v, c, s = map(int, nums)
        else:
            bot.send_message(m.chat.id, 'Неправильный запрос')
            return
        # print(v, c, s)
        if v < 3 or v > 5 or c < 4 or c > 6 or s > 1 or (v + c + s != 9):
            bot.send_message(m.chat.id, 'Числа не подходят под правила')
            return

        vs = np.random.choice(vowels, v, p=vowels_weights)
        cs = np.random.choice(consonants, c, p=consonants_weights)
        ss = np.random.choice(specials, s, p=specials_weights)

        ls = np.hstack((vs, cs, ss))
        # print(vs, cs, ss, ls)

        current_letters = Counter(ls)
        out = ' '.join(ls)
        bot.send_message(m.chat.id, out)


    except Exception as e:
        bot.send_message(m.chat.id, 'Что-то пошло не так')
        raise e


@bot.message_handler(commands=["проверь"])
def start(m):
    try:
        if current_letters is None:
            bot.send_message(m.chat.id, 'Буквы не выбраны')
            return
        # print('буквы есть', flush=True)
        txt = process_message(m)
        if len(txt) > 9:
            bot.send_message(m.chat.id, 'Много букв')
            return
        # print('норм букв', flush=True)
        letters = Counter(txt)
        if letters - current_letters:
            bot.send_message(m.chat.id, 'Неправильные буквы')
            return
        # print('правильные буквы', flush=True)
        if txt not in dictionary:
            bot.send_message(m.chat.id, 'Слова нет в словаре')
            return
        # print('есть в словаре', flush=True)
        bot.send_message(m.chat.id, f'Подходит! {len(txt)} очков')

    except Exception as e:
        bot.send_message(m.chat.id, 'Что-то пошло не так')
        raise e


bot.polling(none_stop=True, interval=0)

bot.set
