import typing as t
from telebot import types


def build_reply_markup(
        button_list: t.Iterable[str],
        one_time_keyboard: bool = True,
        row_width: int = 2,
        resize_keyboard: bool = True
) -> types.ReplyKeyboardMarkup:
    """
    This function builds a reply markup for the bot.
    Here is an example of how to use it:

    YES_NO = ("Yes", "No")

    markup = build_reply_markup(constants.YES_NO)

    msg = bot.reply_to(
        initialMessage,
        "Do you want to continue?",
        reply_markup=markup
    )

    It will return a markup (table) with two buttons: "Yes" and "No".
    You can use it to quickly create reply buttons for the bot.

    Args:
        button_list (tuple[str]):
            It is a tuple of strings. Each string is a button.
        one_time_keyboard (bool, optional):
            Defaults to True.
        row_width (int, optional):
            It is a number of buttons in a row. Defaults to 2.
        resize_keyboard (bool, optional):
            It is a flag to resize the keyboard. Defaults to True.

    Returns:
        types.ReplyKeyboardMarkup: _description_
    """
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=resize_keyboard,
        row_width=row_width,
    )

    buttons = [types.KeyboardButton(i) for i in button_list]
    markup.add(*buttons)

    return markup
