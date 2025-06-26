import sqlite3
import bcrypt

class UserModel:
    def __init__(self, conn):
        self.conn = conn
        self.create_user_table()

    def create_user_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_user(self, username, password):
        password_hash = self.hash_password(password)
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verify_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        if row:
            stored_hash = row[0]
            return self.check_password(password, stored_hash)
        return False

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @staticmethod
    def check_password(password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))