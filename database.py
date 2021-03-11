import sqlite3


class Database():
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.connecion = sqlite3.connect(dbName)
        self.cursor = self.connecion.cursor()
        self.cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.tableName}(name VARCHAR, mobile INTEGER)"""
        )

        self.connecion.commit()
        print(self.connecion)

    def add_data(self, name, mobile):
        self.connecion.execute(f"INSERT INTO {self.tableName} VALUES ('{name}', {mobile})")
        self.connecion.commit()
        return self.connecion.close()
    def fetchAll(self):
        result = self.cursor.execute(f"SELECT * FROM {self.tableName}")
        self.connecion.commit()
        return result
    def tables(self):
        self.cursor.description()


db = Database("db4", 'kalim4')
db.add_data("sdf", 122554)
for i in db.fetchAll():
    print(i)






