import sqlite3
import os

class POSDatabase:
    def __init__(self, db_path="K'iosk.db"):
        self.db_path = db_path
        self.conn = None

    def initialize(self):
        """Create products table if it doesn't exist."""
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        self.conn.commit()

    def get_product_count(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM products")
        return cursor.fetchone()[0]