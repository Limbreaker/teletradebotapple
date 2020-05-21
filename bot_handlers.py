from bot import bot
from messages import HELLO_MESSAGE, MESSAGES, STATE
from telebot import types
import json


@bot.message_handler(commands=['start'])
# Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    list1 = []
    index = 1
    len1 = len(MESSAGES)
    for name in MESSAGES:
        if len1 % 2 == 0:
            list1.append(str(name))
            if len(list1) == 2:
                item1 = types.KeyboardButton(list1[0])
                item2 = types.KeyboardButton(list1[1])
                markup.add(item1, item2)
                list1 = []

        else:
            if index == len1:
                item3 = types.KeyboardButton(str(name))
                markup.add(item3)
            else:
                index += 1
                list1.append(str(name))
                if len(list1) == 2:
                    item1 = types.KeyboardButton(list1[0])
                    item2 = types.KeyboardButton(list1[1])
                    markup.add(item1, item2)
                    list1 = []
    markup.add('Оставить заявку✉')
    bot.send_message(message.chat.id, HELLO_MESSAGE + 'Для начала выберите модель:', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    list1 = []
    list2 = []
    list3 = None
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    for name in MESSAGES:
        # Первая проверка
        if message.text == name:
            with open("data.json", "r") as read_file:
                data = json.load(read_file)
            if f'{message.from_user.id}{message.from_user.username}' in data:
                new_count = data[f'{message.from_user.id}{message.from_user.username}'][1]
                new_count += 1
                data[f'{message.from_user.id}{message.from_user.username}'][1] = new_count
            else:
                data[f'{message.from_user.id}{message.from_user.username}'] = [None, count3]
            for k in data:
                if k != 'count':
                    count1 += data[k]

            if count1 - data['count'] >= 10:
                data['count'] = count1
                bot.send_message(418600901, f"{data}")
            with open("data.json", "w") as write_file:
                json.dump(data, write_file)
            for name1 in MESSAGES[name]:
                count += 1
            if count % 2 == 0:
                for name1 in MESSAGES[name]:
                    list1.append(name1)
                    if len(list1) == 2:
                        markup.add(list1[0], list1[1])
                        list1 = []
                markup.add('/start', 'Оставить заявку✉')
            else:
                for name1 in MESSAGES[name]:
                    list1.append(name1)
                    if len(list1) == 2:
                        markup.add(list1[0], list1[1])
                        list1 = []
                markup.add(list1[0], '/start')
                markup.add('Оставить заявку✉')
            bot.send_message(message.chat.id, 'Выберите количество памяти: ', reply_markup=markup)
        for name2 in MESSAGES[name]:
            # Вторая проверка
            if message.text == name2:
                for name3 in MESSAGES[name][name2]:
                    markup.add(name3)
                markup.add('/start', 'Оставить заявку✉')
                bot.send_message(message.chat.id, 'Выберите состояние, в котором пребывает Ваш телефон: ', reply_markup=markup)
                for k,v in STATE.items():
                    bot.send_message(message.chat.id, f'<b>{k}</b>: {v}\n', parse_mode='html')
            for name3 in MESSAGES[name][name2]:
                if message.text == name3:
                    markup.add('Оставить заявку✉')
                    markup.add('/start')
                    if message.from_user.username is None:
                        bot.send_message(message.chat.id, f'<b>Cпасибо, Ваше сообщение получено!\n</b>'
                                                              f'<b>Детали:</b> {name3} \n'
                                                              f'<b>Средняя стоимость:</b> {MESSAGES[name][name2][name3]} \n'
                                                              f'Но мы заметили что у Вас нету логина @Telegram\n'
                                                              f'Введите Ваш номер телефона: (В формате 380ХХХХХХХХХ)',
                                             parse_mode='html', reply_markup=markup)
                        bot.send_message(725423821,
                                             f'<b>{message.from_user.id} {message.from_user.username} отправил сообщение!</b> \n'
                                             f'<b>Детали:</b> {name3} \n'
                                             f'<b>Cтоимость:</b> {MESSAGES[name][name2][name3]}',
                                             parse_mode='html')
                    else:
                        bot.send_message(message.chat.id, f'<b>Cпасибо, Ваше сообщение получено!\n</b>'
                                                              f'<b>Детали:</b> {name3} \n'
                                                              f'<b>Средняя стоимость:</b> {MESSAGES[name][name2][name3]} \n'
                                                              f'Для более детального обсуждения: 0688815538 или оставьте заявку и мы свяжемся с Вами в течении 30 минут😉',
                                             parse_mode='html', reply_markup=markup)
                        bot.send_message(725423821, f'<b>{message.from_user.id} {message.from_user.username} отправил сообщение!</b> \n'
                                                        f'<b>Детали:</b> {name3} \n'
                                                        f'<b>Cтоимость: </b> {MESSAGES[name][name2][name3]}' ,parse_mode='html')

                    break

    if message.text != '/start':
        list11 = []
        list12 = []
        list13 = []
        list14 = []
        for name in MESSAGES:
            list11.append(name)
            for name1 in MESSAGES[name]:
                list12.append(name1)
                for name2 in MESSAGES[name][name1]:
                    list13.append(name2)
        if '380' in str(message.text) and len(str(message.text)) == 12:
            markup.add('/start')
            bot.send_message(message.chat.id, 'Ваш номер телефона принят. \n'
                                                  'Ожидайте ответа!',
                                 parse_mode='html')
            bot.send_message(725423821,
                             f'<b>{message.from_user.id} отправил номер телефона - {message.text}</b> \n', parse_mode='html', reply_markup=markup)
            with open("data.json", "r") as read_file:
                data = json.load(read_file)
            if f'{message.from_user.id}{message.from_user.username}' in data:
                data[f'{message.from_user.id}{message.from_user.username}'][0] = str(message.text)
            with open("data.json", "w") as write_file:
                json.dump(data, write_file)
        elif message.text == "Оставить заявку✉":
            markup.add('/start')
            bot.send_message(message.chat.id, 'Напишите Ваш номер телефона:\n'
                                              '(В формате 380ХХХХХХХХХ)',
                             parse_mode='html', reply_markup=markup)

        elif message.text not in list11 and message.text not in list12 and message.text not in list13:
            bot.send_message(message.chat.id, 'Я Вас не понял 😥 \n'
                                              'Нажмите на элемент клавиатуры либо введите сообщение /start для возврата в начало', parse_mode='html')



