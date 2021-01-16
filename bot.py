from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ParseMode
from random import seed
from random import random
import logging
import configparser as cfg
import response

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")

# def press_button_callback(bot, update):
#     seed(1)
#     keyboard = [
#                 [InlineKeyboardButton('1' , callback_data='callback_1')],
#                 [ ('2 ', callback_data='callback_2')]
#             ]

#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.callback_query.edit_message_reply_markup(reply_markup)

def create_reply(update, context):
    """Create reply to user."""

    # button = response.create_button(update.message.text)
    reply = response.create_reply(update.message.text)
    update.message.reply_text(reply, 
                    reply_markup=None, 
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def read_token(config_file):
    parser = cfg.ConfigParser()
    parser.read(config_file)
    return parser.get("creds", "token")

def main():
    """Start the bot."""
    token = read_token("config.cfg")
    updater = Updater("1551790980:AAHjHzeeH6qElZid9uLw7IVBrXdSOVSUtZ4", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CallbackQueryHandler(press_button_callback))
    dp.add_handler(MessageHandler(Filters.text, create_reply))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    main()