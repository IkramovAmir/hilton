import hashlib
import mysql.connector


class DB:
    
    def __init__(self, host: str, port: str, user: str, password: str, db_name: str):
        self.__connection: mysql.connector.connection.MySQLConnection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        if not self.__connection.is_connected():
            raise mysql.connector.Error("Connection Error")
        self.cursor: mysql.connector.cursor.MySQLCursor = self.__connection.cursor()

        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.cursor.execute(f"USE {db_name}")
        self.__start()

    def __start(self):
        self.__create_user_table()
        self.__create_room_table()
        self.__create_book_table()

    def __create_user_table(self):
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

    def __create_room_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                id INT AUTO_INCREMENT PRIMARY KEY,
                number INT NOT NULL,
                type VARCHAR(32) NOT NULL,
                space TINYINT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                UNIQUE(number)
            );
        """)
        self.commit()

    def __create_book_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                room_id INT NOT NULL,
                days VARCHAR(512)
            );
        """)
        self.commit()

    def get_user(self, username: str, password: str):
        password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        return self.cursor.fetchone()

    def commit(self):
        self.__connection.commit()
    
    def close(self):
        self.cursor.close()
        self.__connection.close()


class User:
    
    def __init__(self, name: str, phone: str, username: str, password: str):
        self.name = name
        self.phone = phone
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
    
    def save(self, db: DB) -> int:
        db.cursor.execute(
            """INSERT INTO users (name, phone, username, password)
            VALUES (%s, %s, %s, %s);""",
            (self.name, self.phone, self.username, self.password)
        )
        db.commit()


class Room:
    pass


class Book:
    pass

