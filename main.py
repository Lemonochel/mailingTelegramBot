from config import ADMIN_ID, BOT_TOKEN
from users import create_tables, register_user, get_users_info
from defs import set_state_mailing, set_state_default, get_state
import telebot


bot = telebot.TeleBot(BOT_TOKEN)

create_tables()


@bot.message_handler(commands=["start"])
def start_message(message):
    register_user(message.from_user.id, message.from_user.username,
                  message.from_user.first_name, message.from_user.last_name)


@bot.message_handler(commands=["mail"])
def mailing(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(ADMIN_ID, "Введите текст для рассылки:")
        set_state_mailing()


@bot.message_handler(commands=["mail_exit"])
def mail_stop(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(ADMIN_ID, "Рассылка отменена")
        set_state_default()


@bot.message_handler(content_types=["text", "video", "photo"])
def text_handler(message):
    if message.chat.id == ADMIN_ID:
        if get_state() == "mailing":
            for user in get_users_info():
                try:
                    bot.forward_message(user[0], ADMIN_ID, message.message_id)
                except Exception:
                    pass
            set_state_default()


bot.polling()
