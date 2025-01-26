import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = str(os.environ['TOKEN'])
ADMIN_ID = int(os.environ['ADMIN_ID'])
COMMANDS_PATH = str(os.environ['COMMANDS_PATH'])
ALL_TEXT_MESSAGES_WAY = str(os.environ['ALL_TEXT_MESSAGES_WAY'])
if ALL_TEXT_MESSAGES_WAY not in ['copy', 'forward']:
    txt = 'Ошибка чтения переменных окружения. Переменная ALL_TEXT_MESSAGES_WAY не равна copy или forward.'
    raise Exception(txt)


import telebot

bot = telebot.TeleBot(TOKEN)


import json

with open(COMMANDS_PATH, 'r', encoding='utf-8') as json_file:
    TEXT = json.load(json_file)
