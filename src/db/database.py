import sqlite3

DB_name = "finance.db"

def db_init():
    connection = sqlite3.connect(DB_name)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id, INTEGER,
            amount REAL,
            date TEXT
        )
    ''')
    connection.commit()
    connection.close()
    
def add_expenses(user_id, amount, date):
    connection = sqlite3.connect(DB_name)
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO expenses (user_id, amount, date)
        VALUES (?, ?, ?)
    ''', (user_id, amount, date))
    connection.commit()
    connection.close()
    
def get_expenses(user_id):
    connection = sqlite3.connect(DB_name)
    cursor = connection.cursor()
    cursor.execute('SELECT amount, date FROM expenses WHERE user_id = ?', (user_id,))
    result = cursor.fetchall()
    connection.close()
    return result