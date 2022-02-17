import mysql.connector

class Database:
    def __init__(self) -> None:
        self.connector = mysql.connector.connect(
            host=" sql596.main-hosting.eu",
            port=3306,
            user="u830057007_root",
            password="@ugMG123",
            database="u830057007_augmg")


    def getData(self):
        self.cur = self.connector.cursor(buffered=True)
        self.cur.execute("SELECT product_type, product_id, product_desc, image_url FROM products")
        rows = self.cur.fetchall()
        self.cur.close()
        self.connector.close()
        print(rows)
        return rows