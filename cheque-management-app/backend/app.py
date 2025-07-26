from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cheque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    given_date = db.Column(db.String, nullable=False)
    bank = db.Column(db.String, nullable=False)
    cheque_number = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    shop_name = db.Column(db.String, nullable=False)
    salesman_name = db.Column(db.String, nullable=False)
    clear_date = db.Column(db.String, nullable=True)
    remarks = db.Column(db.String, nullable=True)

@app.route('/cheques', methods=['POST'])
def add_cheque():
    data = request.json
    new_cheque = Cheque(
        given_date=data['given_date'],
        bank=data['bank'],
        cheque_number=data['cheque_number'],
        amount=data['amount'],
        shop_name=data['shop_name'],
        salesman_name=data['salesman_name'],
        clear_date=data.get('clear_date'),
        remarks=data.get('remarks')
    )
    db.session.add(new_cheque)
    db.session.commit()
    return jsonify({'message': 'Cheque added successfully'}), 201

@app.route('/cheques', methods=['GET'])
def get_cheques():
    cheques = Cheque.query.all()
    return jsonify([{
        'given_date': cheque.given_date,
        'bank': cheque.bank,
        'cheque_number': cheque.cheque_number,
        'amount': cheque.amount,
        'shop_name': cheque.shop_name,
        'salesman_name': cheque.salesman_name,
        'clear_date': cheque.clear_date,
        'remarks': cheque.remarks
    } for cheque in cheques]), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)