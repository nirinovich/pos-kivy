import sqlite3

class ProductModel:
    def __init__(self, conn):
        self.conn = conn
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, price FROM products")
        return cursor.fetchall()

    def add(self, name, price):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def update(self, product_id, name, price):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE products SET name=?, price=? WHERE id=?", (name, price, product_id))
        self.conn.commit()

    def delete(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        self.conn.commit()