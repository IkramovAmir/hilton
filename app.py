from flask import (
    Flask,
    render_template,
    request,
    session,
)
import settings
from db import DB, User


app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

db = DB(
    host=settings.HOST, 
    port=settings.DB_PORT, 
    user=settings.DB_USER, 
    password=settings.DB_PASSWORD, 
    db_name=settings.DB_NAME
)

@app.route('/')
def home_view():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register_view():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    pass

@app.route('/logout', methods=['POST'])
def logout_view():
    pass

@app.route('/rooms')
def rooms_view():
    pass


if __name__ == "__main__":
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )
