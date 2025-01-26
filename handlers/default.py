from telebot import TeleBot, types

from config import TEXT


def start_command(message: types.Message, bot: TeleBot):
    bot.send_message(message.from_user.id, TEXT['start'])


def help_info_command(message: types.Message, bot: TeleBot):
    bot.send_message(message.from_user.id, TEXT['help_info'])


def non_text_message(message: types.Message, bot: TeleBot):
    bot.send_message(message.from_user.id, TEXT['non_text_message_error'])
