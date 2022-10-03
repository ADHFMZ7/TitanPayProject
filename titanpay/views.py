from flask import render_template, request, redirect, flash
from flask_login import LoginManager, login_required, login_user
from titanpay import app
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
    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        print(user)
        if user:
            if user.pword == password:
                login_user(user)
                return redirect("/transaction")
            else:
                flash("Wrong password. Try again.")
        else:
            flash("User does not exits. Try again.")
        
        return redirect("/signup") 
            
    return render_template("index.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
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