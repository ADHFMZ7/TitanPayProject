from titanpay import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(20), unique=True, nullable=False)
    pword = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    country = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(20), unique=True, nullable=False)
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