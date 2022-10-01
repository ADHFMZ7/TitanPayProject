from dataclasses import dataclass
import sqlite3
from flask import Flask, render_template, request, redirect, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "asdfgjgh"

#models
accounts = {}

@dataclass
class Account:
    name    : str
    pword   : str
    name    : str
    phone   : str
    country : str 
    address : str

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
        user = request.form["username"]
        pword = request.form["password"]
        name = request.form["fullname"]
        phone = request.form["phone"]
        country= request.form["country"]
        address= request.form["address"]
        accounts[user] = Account(user, pword, name, phone, country, address)
        flash("Account Created. Please Login.")
        return redirect("\login") 
    return render_template("signup.html")

def valid(username, password):
    flash("Login Failed. Please Sign Up First")
    return username in accounts.keys() and accounts[username].pword == password 

