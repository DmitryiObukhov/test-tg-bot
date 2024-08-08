import telebot

from utils import build_reply_markup


API_KEY = "YOUR_API_KEY"
MAIN_SCREEN_BUTTON = ('YES', 'NO')

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["start"])
def start(message) -> None:
    markup = build_reply_markup(MAIN_SCREEN_BUTTON)
    bot.send_message(
        message.chat.id,
        "HELLO",
        reply_markup=markup,
    )


bot.polling(none_stop=True)
