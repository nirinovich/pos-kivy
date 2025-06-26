import sqlite3

class CategoryModel:
    def __init__(self, conn):
        self.conn = conn
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        return cursor.fetchall()

    def add(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        self.conn.commit()