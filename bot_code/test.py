import unittest
from unittest.mock import patch, Mock
from bot import start


class TestHandlers(unittest.TestCase):

    @patch("bot.telebot.TeleBot.send_message")
    @patch("bot.utils.build_reply_markup")
    def test_start_message_handler_initial(self, mock_build_reply_markup, mock_send_message):
        mock_build_reply_markup.return_value = "Mocked Markup"
        start(Mock())
        mock_build_reply_markup.assert_called_once_with(("YES", "NO"))
        mock_send_message.assert_called_once_with(
            Mock().chat.id,
            "HELLO",
            reply_markup="Mocked Markup"
        )

    @patch("bot.telebot.TeleBot.send_message")
    @patch("bot.utils.build_reply_markup")
    def test_start_message_handler_final(self, mock_build_reply_markup, mock_send_message):
        mock_build_reply_markup.return_value = "Mocked Markup"
        start(Mock())
        mock_build_reply_markup.assert_called_once_with(("YES", "NO"))
        mock_send_message.assert_called_once_with(
            Mock().chat.id,
            "HELLO",
            reply_markup="Mocked Markup"
        )


if __name__ == '__main__':
    unittest.main()
