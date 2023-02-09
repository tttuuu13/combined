# coding=utf8
from PIL import Image
import telebot
from telebot import types
import os
from flask import Flask, request
import math
import json
from words import word, word_only, word_with_boats, word_with_drops, text
from dtb import *
import datetime


server = Flask(__name__)
TOKEN = '1630813007:AAHf-fp39lyBWuDWxLXthnHKgWMdRcmeUB0'
admins = [599040955]
members_dict = {}
bot = telebot.TeleBot(TOKEN)
start_menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
b1 = types.KeyboardButton(text='Изменить вид слов')
b2 = types.KeyboardButton(text='Ввести текст')
start_menu.add(b2, b1)


#АДМИН
@bot.message_handler(commands=['admin'])
def menu(message):
    if message.chat.id not in admins:
        bot.send_message(chat_id=message.chat.id, text="Эта команда только для админов")
        return
    markup = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton(text='Добавить пользователя', callback_data='add_user')
    b2 = types.InlineKeyboardButton(text='Удалить кого-нибудь', callback_data='delete_user')
    b3 = types.InlineKeyboardButton(text='Доступ на день', callback_data='trial')
    markup.add(b1, b2, b3)
    bot.send_message(chat_id=message.chat.id, text='Главное меню администратора', reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data == 'add_user')
def ask_for_message(query):
    bot.send_message(chat_id=query.message.chat.id, text='Отлично, теперь перешлите мне любое сообщение от пользователя, которого хотите добавить. Только так я смогу узнать его айди')
    message = query.message
    bot.register_next_step_handler(message, ask_name)

def ask_name(message):
    try:
        id = message.forward_from.id
        print(id)
    except Exception as e: 
         bot.send_message(chat_id=message.chat.id, text=f'Не похоже на пересланное сообщение...\nПопробуйте снова {e}')
         menu(message)
         return
    try:
        if id not in get_ids():
            add_user(id)
        enable_premium(id, str(datetime.date.today()))
        bot.send_message(chat_id=message.chat.id, text=f'Успех!')
        bot.send_message(chat_id=message.chat.id, text=f'ID: {id}')
        bot.send_message(chat_id=id, text='🎉Ура! Подписка активирована.\nПриглашайте коллег в бота, больше людей - стабильнее бот', reply_markup=start_menu)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f'Что-то не так, попробуйте еще раз. Ошибка {e}')
        menu(message)


@bot.callback_query_handler(lambda query: query.data == 'trial')
def ask_for_message_trial(query):
    bot.send_message(chat_id=query.message.chat.id, text='Отлично, теперь перешлите мне любое сообщение от пользователя, которого хотите добавить. Только так я смогу узнать его айди')
    message = query.message
    bot.register_next_step_handler(message, ask_name_trial)

def ask_name_trial(message):
    try:
        id = message.forward_from.id
        print(id)
    except Exception as e: 
         bot.send_message(chat_id=message.chat.id, text=f'Не похоже на пересланное сообщение...\nПопробуйте снова {e}')
         menu(message)
         return
    try:
        if id not in get_ids():
            add_user(id)
        enable_premium(id, str(datetime.date.today() - datetime.timedelta(days=29)))
        bot.send_message(chat_id=message.chat.id, text=f'Успех!')
        bot.send_message(chat_id=message.chat.id, text=f'ID: {id}')
        bot.send_message(chat_id=id, text='🎉Ура! Вы получили пробный доступ к боту на день.\nВведите любое слово или нажмите кнопку ввести текст', reply_markup=start_menu)
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f'Что-то не так, попробуйте еще раз. Ошибка {e}')
        menu(message)
        

@bot.message_handler(commands=['users'])
def answer(message):
    paid = [i for i in get_ids() if is_pro(i) == True]
    bot.send_message(message.chat.id, f"Пользователей всего: {len(get_ids())}, из них с активной подпиской: {len(paid)}")

@bot.callback_query_handler(lambda query: query.data == 'delete_user')
def users_list(query):
    users = []
    for i in get_ids():
        if is_pro(i) == True:
            users.append(i)
    markup = types.InlineKeyboardMarkup(row_width=1)
    for user in sorted(users):
        markup.add(types.InlineKeyboardButton(text=user, callback_data=f'delete_{user}'))
    bot.send_message(chat_id=query.message.chat.id, text='Нажмите на пользователя, которого хотите удалить', reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data[:6] == 'delete')
def delete(query):
    if disable_premium(query.data[7:]):
        bot.send_message(query.message.chat.id, text=f'Пользователь {query.data[7:]} успешно удален')
    else:
        bot.send_message(chat_id=query.message.chat.id, text='Что-то не так, попробуйте еще раз')
        menu(query.message)



#ДОСТУП
def is_pro(id):
    if id == '599040955':
        return True
    info = get_info(id)
    if info == None:
        add_user(id)
        return "no"
    if info[2] == None:
        return "no"
    date = datetime.datetime.strptime(info[2], "%Y-%m-%d").date()
    diff = (datetime.date.today() - date).days
    if diff > 30:
        return "expired"
    else:
        return True


@bot.message_handler(commands=['start'])
def answer(message):
    global start_menu
    bot.send_message(chat_id=message.chat.id, text='Приветствую! Отправьте мне любое слово и увидите магию! По вопросам и предложениям пишите @tttuuu13', reply_markup=start_menu)


@bot.message_handler(commands=['text'])
def is_available(message):
    r = is_pro(message.chat.id)
    write_me = types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="НАПИСАТЬ", url="tg://user?id=599040955")]])
    if r == True:
        ask_text(message)
    elif r == "no":
        bot.send_message(chat_id=message.chat.id, text="❗Напишите мне для того, чтобы продолжить пользоваться ботом❗", reply_markup=write_me)
        return
    elif r == "expired":
        bot.send_message(chat_id=message.chat.id, text="💔Похоже ваша подписка закончилась, напишите мне", reply_markup=write_me)
        return


def ask_text(message):
    global exit
    exit = False
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton(text='Выход', callback_data='Выход')
    markup.add(item)
    bot.send_message(chat_id=message.chat.id, text='⭕Для переноса строки на телефоне нажмите enter, на компьютере - shift+enter.\n⭕Используйте один или два символа "_" для выделение нового обзаца\n⭕Вы можете использовать разные регистры букв, точки, запятые, вопросительные и восклицательные знаки.\n⭕Чтобы в дальнейшем использовать генерацию текста просто отправьте боту команду /text.\n⭕Нажмите "Выход", если хотите выйти', reply_markup=markup)
    bot.send_message(chat_id=message.chat.id, text='📝Отправьте текст👇')
    bot.register_next_step_handler(message, ask_size)

def ask_size(message):
    if exit:
        return
    global text1
    text1 = message.text
    #bot.send_message(chat_id=599040955, text=text1)
    bot.send_message(chat_id=message.chat.id, text='Вы можете выбрать размер текста. Средний - 25. Отправьте просто число')
    bot.register_next_step_handler(message, ask_orientation)

def ask_orientation(message):
    if exit:
        return
    global size
    try:
        size = int(message.text)
    except:
        bot.send_message(chat_id=message.chat.id, text='Введите число')
        bot.register_next_step_handler(message, ask_orientation)
        return
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton('Альбомная')
    item2 = types.KeyboardButton('Книжная')
    markup.add(item1, item2)
    bot.send_message(chat_id=message.chat.id, text='Выберите ориентацию', reply_markup=markup)
    bot.register_next_step_handler(message, create_text)

def create_text(message):
    if exit:
        return
    global orientation
    orientation = message.text.lower()
    if orientation == 'альбомная' or orientation == 'книжная':
        pass
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        item1 = types.KeyboardButton('Альбомная')
        item2 = types.KeyboardButton('Книжная')
        markup.add(item1, item2)
        bot.send_message(chat_id=message.chat.id, text='Выберите ориентацию, нажимая на кнопки внизу', reply_markup=markup)
        bot.register_next_step_handler(message, ask_orientation)
        return
    with open('preferences.txt', 'r') as prf:
        prfs = eval(prf.read())
    if str(message.chat.id) in prfs.keys():
        mode = prfs[str(message.chat.id)]
    else:
        mode = 'Обычный'
    try:
        msg = bot.send_message(chat_id=message.chat.id, text='Ожидайте, процесс может занять какое-то время🕒')
        photo, text2 = text(text1, size, orientation, mode)
        photo.save('текст.png')
        photo = open('текст.png', 'rb')
        bot.send_document(chat_id=message.chat.id, document=photo, caption=text1[:10] + '...')
        while text2 != '':
            photo, text2 = text(text2, size, orientation, mode)
            print(text2)
            photo.save('текст.png')
            photo = open('текст.png', 'rb')
            bot.send_document(chat_id=message.chat.id, document=photo, caption='Продолжение')
        bot.edit_message_text(text='Готово!', chat_id=message.chat.id, message_id=msg.id)
        bot.send_message(text='Возврат в меню...', chat_id=message.chat.id, reply_markup=start_menu)
    except:
        bot.delete_message(chat_id=message.chat.id, message_id=msg.id)
        bot.send_message(chat_id=message.chat.id, text='Произошла ошибка, попробуйте еще раз. В тексте допускаются знаки:\n!\n,\n?\n""\n_\n-\n.\n;\n:\n Заглавные и строчные буквы русского алфавита')
        bot.send_message(text='Возврат в меню...', chat_id=message.chat.id, reply_markup=start_menu)

@bot.message_handler(func=lambda m: m.text == 'Ввести текст')
def generate_text(message):
    is_available(message)

@bot.message_handler(func=lambda m: m.text == 'Изменить вид слов')
def change_word(message):
    choose = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    b1 = types.KeyboardButton(text='Обычный')
    b2 = types.KeyboardButton(text='Только буквы')
    b3 = types.KeyboardButton(text='Буквы и капельки')
    b4 = types.KeyboardButton(text='Буквы и лодочки')
    choose.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, 'Выберитe:', reply_markup=choose)
    bot.register_next_step_handler(message, commit)
def commit(message):
    if message.text in ['Обычный', 'Только буквы', 'Буквы и капельки', 'Буквы и лодочки']:
        with open('preferences.txt', 'r') as prf:
            prfs = eval(prf.read())
        with open('preferences.txt', 'w') as prf:
            prfs[str(message.chat.id)] = message.text
            prf.write(str(prfs))
        bot.send_message(message.chat.id, 'Готово!', reply_markup = types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Возвращение в меню...', reply_markup=start_menu)
    else:
        change_word(message)

@bot.message_handler(func=lambda m: m.text[:4]== 'spam')
def spam(message):
    text = message.text[4:]
    ids = admins + get_ids()
    for id in ids:
        print(id)
        bot.send_message(int(id), text=text)
    


@bot.message_handler(func=lambda m: True, content_types=['text'])
def create_word(message):
    r = is_pro(message.chat.id)
    write_me = types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="НАПИСАТЬ", url="tg://user?id=599040955")]])
    if r == "no":
        bot.send_message(chat_id=message.chat.id, text="❗Напишите мне для того, чтобы продолжить пользоваться ботом❗", reply_markup=write_me)
        return
    elif r == "expired":
        bot.send_message(chat_id=message.chat.id, text="💔Похоже ваша подписка закончилась, напишите мне", reply_markup=write_me)
        return
    try:
        for i in message.text.split():
            with open('preferences.txt', 'r') as prf:
                prfs = eval(prf.read())
            if str(message.chat.id) in prfs.keys():
                mode = prfs[str(message.chat.id)]
            else:
                mode = 'Обычный'
            if mode == 'Обычный':
                photo, new_line = word(i.lower(), False)
            elif mode == 'Только буквы':
                photo, new_line = word_only(i.lower(), False)
            elif mode == 'Буквы и капельки':
                photo, new_line = word_with_drops(i.lower(), False)
            else:
                photo, new_line = word_with_boats(i.lower(), False)
            #bot.send_photo(chat_id=message.chat.id, photo=photo)
            photo.save(i + '.png')
            photo = open(i + '.png', 'rb')
            bot.send_document(chat_id=message.chat.id, document=photo)
            photo.close()
            os.remove(i + '.png')
    except:
        bot.send_message(chat_id=message.chat.id, text='Произошла ошибка, проверьте отсутствие знаков припинания и латинских букв, либо слово слишком длинное')

@bot.callback_query_handler(lambda query: query.data == 'Выход')
def exit_func(query):
    bot.send_message(text='Возвращение в меню...', chat_id=query.message.chat.id, reply_markup=start_menu)
    global exit
    exit = True
    return

bot.remove_webhook()
bot.infinity_polling()

"""
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://coral-app-83lpo.ondigitalocean.app/' + TOKEN)
    return "!", 200

if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5001)))
"""
