from config import bot, ALL_TEXT_MESSAGES_WAY
from handlers import default, main


# Стандартные команды (/start, /help, /info и все нетекстовые сообщения)
bot.register_message_handler(default.start_command, commands=['start'], pass_bot=True)
bot.register_message_handler(default.help_info_command, commands=['help', 'info'], pass_bot=True)
bot.register_message_handler(default.non_text_message, content_types=['audio', 'document', 'animation', 'game', 'photo', 'sticker', 'video', 
                                                                      'video_note', 'voice', 'location', 'contact', 'venue', 'dice', 'new_chat_members', 
                                                                      'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 
                                                                      'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 
                                                                      'pinned_message', 'invoice', 'successful_payment', 'connected_website', 'poll', 'passport_data', 
                                                                      'proximity_alert_triggered', 'video_chat_scheduled', 'video_chat_started', 'video_chat_ended', 
                                                                      'video_chat_participants_invited', 'web_app_data', 'message_auto_delete_timer_changed', 
                                                                      'forum_topic_created', 'forum_topic_closed', 'forum_topic_reopened', 'forum_topic_edited', 
                                                                      'general_forum_topic_hidden', 'general_forum_topic_unhidden', 'write_access_allowed', 'user_shared', 
                                                                      'chat_shared', 'story'], pass_bot=True)

# Функция, обрабатывающая любой текст, посылаемый боту (для Админов поведение изменено), в том числе и reply
bot.register_message_handler(main.via_copy_message if ALL_TEXT_MESSAGES_WAY == 'copy' else main.via_forward_message, content_types=['text'], pass_bot=True)


if __name__ == '__main__':
    bot.infinity_polling()
