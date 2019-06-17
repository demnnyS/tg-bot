import telebot

bot = telebot.TeleBot('880561198:AAH92lhMwH8luQUGgW4yijXmq1IRQ2Y1XsM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю, щоб дізнатись мої команди введіть "Команди". Чим можу допомогти?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'команди':
        bot.send_message(message.chat.id, 'Адреса: "Адреса"\nКонтактні дані: "Контакти"\nГрафік роботи: "Графік"\nСоціальні мережі: "Мережі"')
    elif message.text.lower() == 'адреса':
        bot.send_message(message.chat.id, 'Volkswagen Центр Херсон знаходиться за адресою:\nмісто Херсон, Миколаївське шосе, 7-й км')
    elif message.text.lower() == 'контакти':
        bot.send_message(message.chat.id, 'Наші контактні дані:\nТелефон +38 050 388 50 51\nЕлектронна пошта salon@volkswagen.ks.ua\nНаш сайт www.volkswagen.ks.ua')
    elif message.text.lower() == 'графік':
        bot.send_message(message.chat.id, 'Наш графік роботи:\nПн - 08:00-18:00\nВт - 08:00-18:00\nСр - 08:00-18:00\nЧт - 08:00-18:00\nПт - 08:00-18:00\nСб - 09:00-15:00\nНд - Непрацюємо')
    elif message.text.lower() == 'мережі':
        bot.send_message(message.chat.id, 'Наші соціальні мережі:\nFacebook: https://www.facebook.com/VolkswagenXEPCOH/ \nInstagram: https://www.instagram.com/volkswagen_center_kherson/ \nTelegram: https://web.telegram.org/#/im?p=@volkswagen_centr_kherson')
    else:
        bot.send_message(message.chat.id, 'Виникла помилка. Будь ласка введіть "/start".')

bot.polling()
