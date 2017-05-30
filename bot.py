from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    logging.info('User {} called /start'.format(update.message.chat.username))
    greeting_text = "Alright mate! How\'s it going? Nice to see you, {}!".format(update.message.chat.first_name)
    update.message.reply_text(greeting_text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info('User {} said: '.format(update.message.chat.username) + user_text)
    update.message.reply_text(user_text)

def main():
    updater = Updater(settings.TELEGRAM_API_KEY)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    logging.info('Bot started')
    main()