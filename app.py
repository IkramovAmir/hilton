from flask import Flask, render_template, request, session, flash, redirect, url_for
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
    if 'user' not in session:
        flash("You must be logged in to view your profile.")
        return redirect(url_for('login_view'))

    username = session['user']
    print(f"Session username: {username}") 
 
    user = db.get_user_by_username(username)
    
    if user:
        print(f"User data from DB: {user}") 
       
        booked_rooms = db.get_booked_rooms(user[0])  
        
        return render_template("profile.html", user=user, booked_rooms=booked_rooms)
    else:
        flash("User not found.")
        return redirect(url_for('login_view'))

@app.route('/logout', methods=['POST'])
def logout_view():
    session.pop('user', None)  
    flash("You have been logged out successfully.")
    return redirect(url_for('home_view'))

if __name__ == "__main__":
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )
