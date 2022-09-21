import time

import config
from config import *
import telebot
import threading

bot = telebot.TeleBot(TELEGRAM_TOKEN)


# /start
@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    """Start message"""
    bot.reply_to(message, 'Hi, how are you?')

@bot.message_handler(commands=['send_image'])
def send_image(message):
    file = open('./image.png','rb')
    bot.send_photo(message.chat.id, file, '<b>CAPTION !!</b>', parse_mode='html')

@bot.message_handler(commands=['send_file'])
def send_file(message):
    file = open('./file.pdf','rb')
    bot.send_document(message.chat.id, file, caption='<b>CAPTION !!</b>', parse_mode='html')

@bot.message_handler(commands=['send_video'])
def send_file(message):
    bot.send_chat_action(message.chat.id, 'upload_video')
    file = open('./video.mp4','rb')
    bot.send_video(message.chat.id, file, caption='<b>Video !!</b>', parse_mode='html')

@bot.message_handler(content_types=['text', 'photo'])
def bot_text_message(message):
    if message.text and message.text.startswith('/'):
        bot.send_message(message.chat.id, 'Unknown command')
    else:
        m = bot.send_message(
            message.chat.id,
            '<u>Subscribe to my channel</u> <a href="google.com">google.com</a>',
            parse_mode='html',
            disable_web_page_preview=False)
        time.sleep(3)
        bot.edit_message_text('<u>Bye !!</u>', message.chat.id, m.message_id, parse_mode='html')
        time.sleep(3)
        bot.delete_message(message.chat.id, m.message_id)
        bot.delete_message(message.chat.id, message.message_id)

def listening_messages():
    bot.infinity_polling()

if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Say hello'),
        telebot.types.BotCommand('/send_video', 'Bot send you a video file'),
        telebot.types.BotCommand('/send_image', 'Bot send you a image file'),
    ])
    print('Starting the bot...')
    thread_bot = threading.Thread(name='Thread for my Bot', target=listening_messages)
    thread_bot.start()
    print('Bot is listening...')
    bot.send_message(CHANNEL_ID,'Hey bro !')
