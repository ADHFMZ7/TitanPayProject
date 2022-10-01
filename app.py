import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = {}

# @app.route('/')
# def index():
#     return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
@app.route('/')
def login():
    

    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")
        if request.form.get("signup") or not valid(username, password):
            global a; a = "Account does not exist. Please create one."
        
            return redirect("/signup") 
        else:
            print("success")
    return render_template("index.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = request.form["username"]
        pword = request.form["password"]
        name = request.form["fullname"]
        phone = request.form["phone"]
        country= request.form["country"]
        address= request.form["address"]
        db[user] = pword
        print(user, pword, name, phone, country, address) 
        return redirect("\login") 
    return render_template("signup.html")

def valid(username, password):
    return username in db and db[username] == password 