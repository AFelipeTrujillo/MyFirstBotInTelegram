from config import *
import telebot
from telebot.types import ForceReply
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Send /submit to create an user')

@bot.message_handler(commands=['submit'])
def cmd_submit(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, 'What is your name?', reply_markup=markup)
    bot.register_next_step_handler(msg, question_age)

def question_age(message):
    name = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, 'how old are you?', reply_markup=markup)
    bot.register_next_step_handler(msg, question_gender)

def question_gender(message):
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, 'This is not a number\nhow old are you?', reply_markup=markup)
        bot.register_next_step_handler(msg, question_gender)
    else:
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="Please choice")
        markup.add("Male", "Female")
        msg = bot.send_message(message.chat.id, 'What is your gender?', reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()