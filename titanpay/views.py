from flask import render_template, request, redirect, flash
from flask_login import LoginManager, login_required
from titanpay import app
from titanpay.models import User, Purchase, create_purchase, create_user, valid

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login', methods=["POST", "GET"])
@app.route('/')
def login():
    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")
        if request.form.get("signup") or not valid(username, password):
            return redirect("/signup") 
        else:
            print("success")
            
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
    return render_template("/transaction") 