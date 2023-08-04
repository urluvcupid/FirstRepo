import telebot
from telebot import types


bot = telebot.TeleBot("6403031621:AAEkqTg_A3xYkjfUDtdF_1mh009K5phmCYg")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет мой создатель {message.from_user.first_name}"\
            f"{message.from_user.last_name}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler(commands=["website"])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(f"Перейти в веб сайт", url="https://www.youtube.com/"))
    bot.send_message(message.chat.id, "Перейти на сайт!", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Hi":
        bot.send_message(message.chat.id, "Bye")

    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, "Кайфы")

