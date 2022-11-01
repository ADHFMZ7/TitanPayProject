from flask import render_template, request, redirect, flash
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from titanpay import app, db
from titanpay.models import User, Purchase, create_purchase, create_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@app.route('/login', methods=["POST", "GET"])
@app.route('/')
def login():
    if current_user.is_authenticated:
        return redirect("/home")
    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        print(user)
        if user:
            if user.pword == password:
                login_user(user, remember=True)
                return redirect("/home")
            else:
                flash("Wrong password. Try again.")
                return redirect("/login")
        else:
            flash("User does not exist. Please sign up.")
        
        return redirect("/signup") 
            
    return render_template("index.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        for x in db.session.query(User):
            if username == x.username:
                flash("username already exists")
                return render_template("signup.html")
        create_user(request)
        flash("Account Created. Please Login.")
        return redirect("\login") 
    return render_template("signup.html")


@app.route('/transaction', methods=["GET", "POST"])
@login_required
def transaction():
    if request.method =="POST":
        create_purchase(request)
        flash("new purchase added")
        return redirect('/home')
    return render_template("transaction.html") 

@app.route('/home', methods=["GET"])
@login_required
def home():
    current_user.calculate_balance()
    return render_template("home.html", cat=None)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Succesfully logged out")
    return redirect('/login')

@app.route("/info")
@login_required
def info():
    return render_template("info.html")