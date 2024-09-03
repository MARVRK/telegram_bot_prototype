import sqlite3
import os.path


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'database.db'))
        self.cur = self.conn.cursor()

    def create_db(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTEGER,
                            gender TEXT,
                            email TEXT,
                            phone_number INTEGER,
                            points INTEGER DEFAULT 1000
                            )''')
        self.conn.commit()

    def insert_database(self, name, age, gender, email, phone_number):
        self.cur.execute('INSERT INTO users(name,age,gender,email,phone_number) VALUES(?,?,?,?,?)',
                         (name, age, gender, email, phone_number))
        self.conn.commit()

    def delete_via_phone_number(self, phone_number):
        self.cur.execute('DELETE FROM users WHERE phone_number =?',
                         (phone_number,))
        self.conn.commit()


db = Database()
db.create_db()
# # db.insert_database("rk", 30,"male",948170)
# db.delete_via_phone_number(948170)
