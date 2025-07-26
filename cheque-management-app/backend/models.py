from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cheque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    given_date = db.Column(db.Date, nullable=False)
    bank = db.Column(db.String(100), nullable=False)
    cheque_number = db.Column(db.String(50), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    shop_name = db.Column(db.String(100), nullable=False)
    salesman_name = db.Column(db.String(100), nullable=False)
    clear_date = db.Column(db.Date, nullable=True)
    remarks = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Cheque {self.cheque_number} - {self.amount}>'