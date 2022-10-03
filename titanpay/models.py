from titanpay import app, db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(20), unique=True, nullable=False)
    pword = db.Column(db.String(60), nullable=False, unique=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(20), unique=False, nullable=False)
    purchases = db.relationship('Purchase', backref='user', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.name}', '{self.phone}')"
    
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    card = db.Column(db.Enum, nullable=False) 
    amount = db.Column(db.Integer, nullable=False) 
    cycle = db.Column(db.String(20), nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Purchase('{self.amount}', '{self.date}', '{self.card}', '{self.paid}')"
    

def create_user(request):
    
    user = User(
        username=request.form["username"],
        pword=request.form["password"],
        name=request.form["fullname"],
        phone=request.form["phone"],
        country=request.form["country"],
        address=request.form["address"]
    )
    
    db.session.add(user)
    db.session.commit()

def create_purchase(request):
    purchase = Purchase(
        date = request.form["date"]
    )