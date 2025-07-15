import requests
from src.db.database import add_expenses, get_expenses

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Я Cash'ик 💸")

    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(message.chat.id, "Команды: /add, /stats, /help")
        
    @bot.message_handler(commands=['add'])
    def add_command(message):
        bot.send_message(message.chat.id, "Введи сумму и дату, когда нужно заплатить, к примеру:\n200 12.05.26")
        bot.register_next_step_handler(message, save_expense)
        
    def save_expense(message):
        try:
            amount_str, date = message.text.split()
            amount = float(amount_str)
            add_expenses(message.from_user.id, amount, date)
            bot.send_message(message.chat.id, "Успешно записано")
        except Exception:
            bot.send_message(message.chat.id, "Ошибка ввода. Попробуй так: 300 07.08.26")
            
    @bot.message_handler(commands=['stats'])
    def show_stats(message):
        rows = get_expenses(message.from_user.id)
        if not rows:
            bot.send_message(message.chat.id, "Нет записей.")
        else:
            text = "\n".join([f"{amount} ₽ — ({date})" for amount, date in rows])
            bot.send_message(message.chat.id, "💰 Подписки:\n" + text)
            
    @bot.message_handler(commands=['wake'])
    def wake_bot(message):
        url = "https://botik-9uuk.onrender.com/ping"
        try:
            requests.get(url)
            bot.send_message(message.chat.id, "🔔 Бот разбужен.")
        except Exception:
            bot.send_message(message.chat.id, "⚠️ Не удалось разбудить сервер.")