
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    name = request.form.get("username") 
    return render_template("login.html", name)

@app.route('/signup', methods=["POST"])
def signup():
    return render_template("signup.html")