from flask import Flask
import settings
from db import DB


app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

db = DB(
    host=settings.HOST, 
    port=settings.DB_PORT, 
    user=settings.DB_USER, 
    password=settings.DB_PASSWORD, 
    db_name=settings.DB_NAME
)


if __name__ == "__main__":
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )
