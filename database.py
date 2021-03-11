import sqlite3


class Database():
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.connecion = sqlite3.connect(dbName)
        self.cursor = self.connecion.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS data (name VARCHAR, mobile INTEGER, products VARCHAR, pieces INTEGER, price INTEGER, day INTEGER, month INTEGER, year INTEGER, address VARCHAR, salesman VARCHAR)"""
        )

        self.connecion.commit()
        print(self.connecion)

    def add_data(self, name, mobile, products, pieces, price, day, month, year, address, salesman):
        self.connecion.execute(f"INSERT INTO data VALUES ('{name}', {mobile}, '{products}', {pieces}, {price}, {day}, {month}, {year}, '{address}', '{salesman}')")
        self.connecion.commit()


db = Database("db.sqlite", "data")
db.add_data("Afzal", 167556465, 'paijama', 5, 1500, 1, 2, 2021, 'mdpur', 'sonu')












