from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#config
app.secret_key = "asdfgjgh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model.db'
db = SQLAlchemy(app)

from titanpay import views