import telebot
from telebot import types

bot = telebot.TeleBot('1808104531:AAFbhg77kO_RX5dMy1ohF9TzNOzbVp12-20')

def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Получить документацию для проекта')
    key2 = types.KeyboardButton('Связаться с менеджером')
    markup.add(key1,key2)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте уважаемый пользователь,пожалуйста выберите интересующий вас раздел', reply_markup=main())

@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == 'Получить документацию для проекта':
        keyboard = telebot.types.InlineKeyboardMarkup()
        switch_button1 = telebot.types.InlineKeyboardButton(text="Фасадные решения", callback_data="var_1")
        keyboard.add(switch_button1)
        switch_button2 = telebot.types.InlineKeyboardButton(text="Светопрозрачные конструкции", callback_data="var_2")
        keyboard.add(switch_button2)
        switch_button3 = telebot.types.InlineKeyboardButton(text="Алюминиевые окна", callback_data="var_3")
        keyboard.add(switch_button3)
        bot.send_message(message.chat.id, "Пожалуйста, выберите сегмент", reply_markup=keyboard)
    elif message.text == 'Связаться с менеджером':
        keyboard = telebot.types.InlineKeyboardMarkup()
        switch_button4 = telebot.types.InlineKeyboardButton(text="Заказать звонок", callback_data="var_4")
        keyboard.add(switch_button4)
        switch_button5 = telebot.types.InlineKeyboardButton(text="Телефон для связи", callback_data="var_5")
        keyboard.add(switch_button5)
        switch_button6 = telebot.types.InlineKeyboardButton(text="Связаться с менеджером в телеграм", callback_data="var_6")
        keyboard.add(switch_button6)
        bot.send_message(message.chat.id, "Пожалуйста,выберите подходящий вам вариант", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Попробуем ещё раз?', reply_markup=main())

@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.data == 'var_1':
        answer = 'ГОСТ на фасадные решения'
        bot.send_message(call.from_user.id, answer)
        bot.send_photo(call.from_user.id, photo=open('test.png', 'rb'))
        doc = open('test.pdf', 'rb')
        bot.send_document(call.from_user.id, doc)
        bot.send_message(call.from_user.id, 'https://internet-law.ru/gosts/gost/69336/')
    elif call.data == 'var_2':
        answer = 'ГОСТ на светопрозрачные конструкции'
        bot.send_message(call.from_user.id, answer)
        bot.send_photo(call.from_user.id, photo=open('test2.png', 'rb'))
        doc = open('test2.pdf', 'rb')
        bot.send_document(call.from_user.id, doc)
        bot.send_message(call.from_user.id, 'https://internet-law.ru/gosts/gost/69667/')
    elif call.data == 'var_3':
        answer = 'ГОСТ на алюминиевые окна'
        bot.send_message(call.from_user.id, answer)
        bot.send_photo(call.from_user.id, photo=open('test3.png', 'rb'))
        doc = open('test.pdf', 'rb')
        bot.send_document(call.from_user.id, doc)
        bot.send_message(call.from_user.id, 'https://internet-law.ru/gosts/gost/8421/')
    elif call.data == 'var_4':
        answer = 'Перейдите на сайт для заполнения формы обратной связи'
        bot.send_message(call.from_user.id, 'https://kramz-trade.ru/backlink')
    elif call.data == 'var_5':
        answer = 'Наш телефон поддержки 8 (391) 226 70 89 '
        bot.send_message(call.from_user.id, answer)
    elif call.data == 'var_6':
        answer = 'Связаться с менеджером напрямую '
        bot.send_message(call.from_user.id, 'https://t.me/Dkorotky')


bot.polling(none_stop=True, interval=0)