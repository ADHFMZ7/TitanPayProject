from flask import render_template, request, redirect, flash
from titanpay import app
from titanpay.models import User, Purchase

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

def valid(username, password):
    return True 
    ret = username in accounts.keys() and accounts[username].pword == password 
    if not ret:
        flash("Login Failed. Please Sign Up First")
    return ret 

def create_user(request):
    
    user = User(
        username=request.form["username"],
        pword=request.form["password"],
        name=request.form["fullname"],
        phone=request.form["phone"],
        country=request.form["country"],
        address=request.form["address"]
    )
    