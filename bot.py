from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ParseMode
from random import random
import logging
import configparser as cfg
import response
import button

def read_token(config_file):
    """Read token from config file."""
    parser = cfg.ConfigParser()
    parser.read(config_file)
    return parser.get("creds", "token")

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def callback_query_handler(update, context):
    cqd = update.callback_query.data
    print(cqd)

    pass # TBD

def reply(update, context, from_callback=False, callback_msg=None):
    """Create reply to user."""
    msg = update.message.text
    reply = response.create_reply(msg)
    reply_markup = button.create_button(msg)
    update.message.reply_text(reply, 
                    reply_markup=reply_markup, 
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True)

def main():
    """Start the bot."""
    print("Bot enabled... press CTRL+C to disabled")
    token = read_token("config.cfg")
    updater = Updater(token, use_context=True)
    bot = updater.bot
    dp = updater.dispatcher
    dp.add_handler(CallbackQueryHandler(callback_query_handler))
    dp.add_handler(MessageHandler(Filters.text, reply))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    main()