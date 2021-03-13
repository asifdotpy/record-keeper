import sqlite3
import datetime

class Database():
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.connecion = sqlite3.connect(dbName)
        self.cursor = self.connecion.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS data (name VARCHAR, mobile VARCHAR, products VARCHAR, pieces INTEGER, price INTEGER, date date, address VARCHAR, salesman VARCHAR, image VARCHAR)"""
        )

        self.connecion.commit()
        print(self.connecion)

    def add_data(self, name, mobile, products, pieces, price, date, address, salesman, image):
        self.connecion.execute(f"INSERT INTO data VALUES ('{name}', {mobile}, '{products}', {pieces}, {price}, '{date}', '{address}', '{salesman}', '{image}')")
        self.connecion.commit()





db = Database("db.sqlite", "data")










