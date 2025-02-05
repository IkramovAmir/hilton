from flask import (
    Flask,
    render_template,
    request,
    session,
    flash,
    redirect,
    url_for,
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
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        
        user = User(
            name=form['name'],
            phone=form['phone'],
            username=form['username'],
            password=form['password']
        )
        try:
            user.save(db)
        except:
            flash("User already exists.")
            return render_template("register.html")

        return redirect(url_for('login_view'))

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        form = request.form

        user = db.get_user(form['username'], form['password'])
        if user:
            session['user'] = form['username']
            return redirect(url_for("profile_view"))
        else:
            flash("Invalid username or password.")
            return render_template('login.html')

@app.route('/profile')
def profile_view():
    pass

@app.route('/logout', methods=['POST'])
def logout_view():
    pass


@app.route('/rooms')
def rooms_view():

    rooms = [
        {
            "id": 1,
            "room_number": 783,
            "description": "fdsfasSome quick example text to build on the card title and make up the bulk of the card's content.",
            "room_floor": 9,
            "room_image": ["img/hilton-banner.avif", "img/hilton-banner.avif",],
            "price":{
                "currency":"usd",
                "amount":90
            },

            "includes": [
                "Good breakfast",
                "Free private parking",
                "Indoor swimming pool",
                "Restaurant",
                "Airport shuttle",
                "Spa and wellness centre",
                "Free WiFi",
                "View",
                "Family rooms",
                "Room service",

            ]

        },
                {
            "id": 1,
            "room_number": 783,
            "description": "fdsfasSome quick example text to build on the card title and make up the bulk of the card's content.",
            "room_floor": 9,
            "room_image": ["img/hilton-banner.avif", "img/hilton-banner.avif",],
            "price":{
                "currency":"usd",
                "amount":90
            },

            "includes": [
                "Good breakfast",
                "Free private parking",
                "Indoor swimming pool",
                "Restaurant",
                "Airport shuttle",
                "Spa and wellness centre",
                "Free WiFi",
                "View",
                "Family rooms",
                "Room service",

            ]

        },
                        {
            "id": 1,
            "room_number": 783,
            "description": "fdsfasSome quick example text to build on the card title and make up the bulk of the card's content.",
            "room_floor": 9,
            "room_image": ["img/hilton-banner.avif", "img/hilton-banner.avif",],
            "price":{
                "currency":"usd",
                "amount":90
            },

            "includes": [
                "Good breakfast",
                "Free private parking",
                "Indoor swimming pool",
                "Restaurant",
                "Airport shuttle",
                "Spa and wellness centre",
                "Free WiFi",
                "View",
                "Family rooms",
                "Room service",

            ]

        },
                                {
            "id": 1,
            "room_number": 783,
            "description": "fdsfasSome quick example text to build on the card title and make up the bulk of the card's content.",
            "room_floor": 9,
            "room_image": ["img/hilton-banner.avif", "img/hilton-banner.avif",],
            "price":{
                "currency":"usd",
                "amount":90
            },

            "includes": [
                "Good breakfast",
                "Free private parking",
                "Indoor swimming pool",
                "Restaurant",
                "Airport shuttle",
                "Spa and wellness centre",
                "Free WiFi",
                "View",
                "Family rooms",
                "Room service",

            ]

        },
        
    ]

    return render_template("rooms.html", rooms=rooms)


if __name__ == "__main__":
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )
