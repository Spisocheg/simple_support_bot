import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = str(os.environ['TOKEN'])
ADMIN_ID = int(os.environ['ADMIN_ID'])
COMMANDS_PATH = str(os.environ['COMMANDS_PATH'])


import telebot

bot = telebot.TeleBot(TOKEN)


import json

with open(COMMANDS_PATH, 'r', encoding='utf-8') as json_file:
    TEXT = json.load(json_file)
