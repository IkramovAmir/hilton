import mysql.connector

class DB:
    
    def __init__(self, host: str, port: str, user: str, password: str, db_name: str):
        self.connection: mysql.connector.connection.MySQLConnection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        if not self.connection.is_connected():
            raise mysql.connector.Error("Connection Error")
        self.cursor: mysql.connector.cursor.MySQLCursor = self.connection.cursor()
        self.db_name = db_name
    
    def create_db(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS %s", (self.db_name,))
        self.commit()

    def create_user_table(self):
        pass

    def create_room_table(self):
        pass

    def create_book_table(self):
        pass

    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()


class User:
    pass


class Room:
    pass


class Book:
    pass

