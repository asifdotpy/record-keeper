import sqlite3
import datetime

class Database():
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.connecion = sqlite3.connect(dbName)
        self.cursor = self.connecion.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS data (image BLOB, 
                                                name VARCHAR, 
                                                mobile VARCHAR, 
                                                products VARCHAR, 
                                                pieces INTEGER, 
                                                price INTEGER, 
                                                date DATE, 
                                                address VARCHAR, 
                                                salesman VARCHAR)"""
        )

        self.connecion.commit()

    def add_data(self, imagePath, name, mobile, products, pieces, price, date, address, salesman):
        with open(imagePath, 'rb') as file:
            image = file.read()
        self.connecion.execute(f"""
                        INSERT INTO data (image, name, mobile, products, pieces, price, date, address, salesman)
                        VALUES (?,?,?,?,?,?,?,?,?);
""", (image, name, mobile, products, pieces, price, date, address, salesman))
        self.connecion.commit()











