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
                price REAL NOT NULL,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT products.id, products.name, products.price, categories.name
            FROM products
            LEFT JOIN categories ON products.category_id = categories.id
        """)
        return cursor.fetchall()

    def add(self, name, price, category_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", (name, price, category_id))
        self.conn.commit()

    def update(self, product_id, name, price, category_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE products SET name=?, price=?, category_id=? WHERE id=?", (name, price, category_id, product_id))
        self.conn.commit()

    def delete(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        self.conn.commit()