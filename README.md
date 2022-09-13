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

