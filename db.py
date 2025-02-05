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

        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.cursor.execute(f"USE {db_name}")
        self.start()

    def start(self):
        self.create_user_table()
        self.create_room_table()
        self.create_book_table()

    def create_user_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(64) NOT NULL,
                phone VARCHAR(13) NOT NULL,
                username VARCHAR(64) NOT NULL ,
                password VARCHAR(255) NOT NULL,
                UNIQUE(username)
            );
        """)
        self.commit()

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

