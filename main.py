from flask import Flask
import threading
from telebot import TeleBot
from src.config.settings import bot_token
from src.bot.handlers import register_handlers
from src.db.database import init_db

# Инициализация бота
bot = TeleBot(bot_token)
register_handlers(bot)
init_db()

# Flask-приложение
app = Flask(__name__)

@app.route('/')
@app.route('/ping')
def ping():
    return '✅ Bot is awake!'

# Отдельный поток для запуска Telegram-бота
def run_telegram():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    threading.Thread(target=run_telegram).start()
    app.run(host='0.0.0.0', port=10000)


