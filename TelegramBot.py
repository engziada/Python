telebot_token='6180652798:AAHGzJQ-e5ve6U2UCi4tgb7vweNO9REp7vE'

import telebot
from telebot import types,util

bot = telebot.TeleBot(telebot_token)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()
