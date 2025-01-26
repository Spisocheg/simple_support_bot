from telebot import TeleBot, types

from config import ADMIN_ID, TEXT


# формат forward_origin.sender_user_name: from_user.id
USERNAMES_IDS = {}


def via_copy_message(message: types.Message, bot: TeleBot):
    '''
    Реализация пересылки сообщений (от Пользователя к Админу) посредством отправки нового сообщения в формате:\n
            [user_id=<ID Пользователя>]\n
            [msg_id=<ID исходного сообщения от Пользователя>]
        
            <текст исходного сообщения от Пользователя>
             
    В таком случае все сообщения от Пользователей будут выглядеть как форматированные новые сообщения.
    
    Для ответа требуется "ответить" на них (reply). Для Пользователя сообщения придут как ответы (reply) на их сообщения.
    '''
    
    msg_id_pattern = '[msg_id='
    user_id_pattern = '[user_id='
        
    def text_from_admin(msg):
        # Если Админ отправляет сообщение без reply
        # или
        # Если Админ отправляет reply на предупреждение бота или какое-то другое сообщение, не пересланное от Пользователя
        if not msg.reply_to_message or (msg_id_pattern not in msg.reply_to_message.text and user_id_pattern not in msg.reply_to_message.text):
            bot.send_message(msg.from_user.id, TEXT['sender_error'])
            return None
        
        # Получение Пользователя (кому ответить) и сообщения (на что ответить)
        user_id = msg.reply_to_message.text.split('\n')[0].replace(user_id_pattern, '').replace(']', '')
        msg_id = msg.reply_to_message.text.split('\n')[1].replace(msg_id_pattern, '').replace(']', '')
        
        # Отправка reply на сообщение Пользователя с ответом Админа
        try:
            bot.send_message(user_id, msg.text, reply_to_message_id=msg_id)
        except Exception:
            bot.send_message(user_id, msg.text)
        
        # Уведомление Админа об отправке ответа Пользователю
        bot.send_message(msg.from_user.id, TEXT['message_sent_to_user'])
    
    def text_from_user(msg):
        # Запрет на использование Пользователем системных конструкций
        if msg_id_pattern in msg.text or user_id_pattern in msg.text:
            bot.send_message(msg.from_user.id, TEXT['pattern_error'])
            return None
        
        # Заготовка для сообщения, где шапка - это информация об отправившем Пользователе, тело - сам текст
        text = f'{user_id_pattern}{msg.from_user.id}]\n{msg_id_pattern}{msg.message_id}]\n\n{msg.text}'
        
        # Отправка сообщения Админу
        bot.send_message(ADMIN_ID, text)
            
        # Уведомление Пользователя, что его сообщение отправлено
        bot.send_message(msg.from_user.id, TEXT['message_sent_to_admin'])
    
    
    if message.from_user.id in [ADMIN_ID]:
        text_from_admin(message)
    else:
        text_from_user(message)


def via_forward_message(message: types.Message, bot: TeleBot):
    '''
    Реализация пересылки (от Пользователя к Админу) посредством отправки forward (пересланного сообщения) Админу.
    
    Поскольку политика приватности позволяет Пользователю при желании скрыть ссылку на свой профиль в "Переслано от ..." 
    (вместо его профиля будет отображаться всплывающее окно "Аккаунт скрыт Пользователем"), поэтому ID для таких Пользователей, куда посылать ответ, 
    хранится в переменной, которая при перезапуске бота будет ОЧИЩАТЬСЯ. Поэтому использовать эту функцию на данном этапе ее разработки не рекомендуется.
    
    Для ответа требуется "ответить" на них (reply). Для Пользователя сообщения придут как новые сообщения.
    '''
    
    def text_from_admin(msg):
        # Если Админ отправляет сообщение без reply
        # или
        # Если Админ отправляет сообщение не на forward от клиента
        if not msg.reply_to_message:
            bot.send_message(msg.from_user.id, TEXT['sender_error'])
            return None

        # Получение Пользователя (кому ответить)
        if msg.reply_to_message.forward_origin.type == 'hidden_user':
            user_id = USERNAMES_IDS[msg.reply_to_message.forward_origin.sender_user_name]
        elif msg.reply_to_message.forward_origin.type == 'user':
            user_id = msg.reply_to_message.forward_origin.sender_user.id
        
        # Отправка ответа Пользователю от Админа
        bot.send_message(user_id, msg.text)
        
        # Уведомление Админа об отправке ответа Пользователю
        bot.send_message(msg.from_user.id, TEXT['message_sent_to_user'])
            
    def text_from_user(msg):
        # Пересылка сообщения от Пользователя Админу
        new_msg = bot.forward_message(ADMIN_ID, msg.from_user.id, msg.message_id)
        
        # Добавление в временный словарь на случай, если пересылки от Пользователя скрыты
        if new_msg.forward_origin.type == 'hidden_user':
            USERNAMES_IDS[new_msg.forward_origin.sender_user_name] = msg.from_user.id
        
        # Уведомление Пользователя, что его сообщение переслано
        bot.send_message(msg.from_user.id, TEXT['message_sent_to_admin'])
    
    
    if message.from_user.id in [ADMIN_ID]:
        text_from_admin(message)
    else:
        text_from_user(message)