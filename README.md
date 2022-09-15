# My First Bot in Telegram with Python

![MyBot](https://i.imgur.com/abgKOuq.gif)

## Create token

1. Got to telegram and find user @BotFather
2. Type /newbot
3. add name and username (have to be unique)
4. then, type /token

## Install pyTelegramBotAPI

```
pip install pyTelegramBotAPI
```

### Usage
```
import telebot
bot = telebot.TeleBot("TOKEN", parse_mode=None)
```

## Create command /start or /help
message_handler
A message handler is a function that is decorated with the message_handler decorator of a TeleBot instance. Message handlers consist of one or multiple filters. Each filter must return True for a certain message in order for a message handler to become eligible to handle that message. A message handler is declared in the following way (provided bot is an instance of TeleBot)
```
@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    """Start message"""
    bot.reply_to(message, 'Hi, how are you?')
```
## How format text in html
```
@bot.message_handler(content_types=['text'])
def bot_text_message(message):
    if not message.text.startswith('/'):
        bot.send_message(
            message.chat.id,
            '<u>Subscribe to my channel</u> <a href="google.com">google.com</a>',
            parse_mode='html',
            disable_web_page_preview=False)
    else:
        bot.send_message(message.chat.id, 'Unknown command')
```
**Note**: you can use markdown as well

## How to edit and delete messages
```
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
```
Check the method **edit_message_text** and **delete_message**

## How to send an image, file and video
Use the method **send_photo**, **send_document** and send_video
```
@bot.message_handler(commands=['send_image'])
def send_image(message):
    file = open('./image.png','rb')
    bot.send_photo(message.chat.id, file, '<b>CAPTION !!</b>', parse_mode='html')
```

```
@bot.message_handler(commands=['send_file'])
def send_file(message):
    file = open('./file.pdf','rb')
    bot.send_document(message.chat.id, file, caption='<b>CAPTION !!</b>', parse_mode='html')
```
```
@bot.message_handler(commands=['send_video'])
def send_file(message):
    file = open('./video.mp4','rb')
    bot.send_video(message.chat.id, file, caption='<b>Video !!</b>', parse_mode='html')
```
## Sending chat action
```
bot.send_chat_action(message.chat.id, 'upload_video')
```
## Create a thread for my bot
```
def listening_messages():
    bot.infinity_polling()

if __name__ == '__main__':
    print('Starting the bot...')
    thread_bot = threading.Thread(name='Thread for my Bot', target=listening_messages)
    thread_bot.start()
    print('end')
```