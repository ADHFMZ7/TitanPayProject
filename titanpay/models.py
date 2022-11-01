from titanpay import app, db
from flask_login import UserMixin, current_user
from datetime import datetime

fees = {
    "amex" : 0.008,
    "visa" : 0.01,
    "discover" : 0.005,
    "convenience_fee" : 0.002
}

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(20), unique=True, nullable=False)
    pword = db.Column(db.String(60), nullable=False, unique=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(20), unique=False, nullable=False)
    purchases = db.relationship('Purchase', backref='user', lazy=True)
   
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def calculate_balance(self):
        balance = 0
        for x in self.purchases:
            if not x.paid:
                balance += x.amount
        print(f"BALANCE IS {balance}")
        return round(balance, 2)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.name}', '{self.phone}')"
    
class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    card = db.Column(db.String(20), nullable=False) 
    amount = db.Column(db.Float, nullable=False) 
    cycle = db.Column(db.String(20), nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Purchase('{self.amount}', '{self.date}', '{self.card}', '{self.paid}', '{self.cycle}')"
    

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
        date = datetime.strptime(request.form["date"], "%Y-%m-%d"),
        card = request.form["card"],
        amount = float(request.form["amount"]) * (1-fees[request.form["card"]]),
        cycle = request.form["date"][:7],
        paid = request.form["paid"] == 'yes',
        user_id = current_user.id
    )
    print(purchase)
    db.session.add(purchase)
    db.session.commit()
    
