from telebot import TeleBot
from src.db.database import db_init
from src.config.settings import bot_token
from src.bot.handlers import register_handlers

bot = TeleBot(bot_token)

db_init()

register_handlers(bot) #регистрация всех хэндлеров

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)

