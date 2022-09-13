import config
from config import *
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)


# /start
@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    """Start message"""
    bot.reply_to(message, 'Hi, how are you?')


@bot.message_handler(content_types=['text'])
def bot_text_message(message):
    if not message.text.startswith('/'):
        bot.send_message(message.chat.id, 'Subscribe to my channel')
    else:
        bot.send_message(message.chat.id, 'Unknown command')

if __name__ == '__main__':
    print('Starting the bot...')
    bot.infinity_polling()
