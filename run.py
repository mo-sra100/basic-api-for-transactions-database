from flask import Flask,render_template,request,redirect, abort
from flask import jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class TransactionsModel(db.Model):
    __tablename__ = "transactions"
    transaction_id = db.Column(db.String, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'transaction_id:{self.transaction_id}, price:{self.price}, date: {self.date}, address:{self.address}'

import sqlite3
conn = sqlite3.connect('transactions.db', check_same_thread=False)
cur1 = conn.cursor()
cur1.execute('SELECT * FROM transactions')
data_columns = cur1.description
data_result = [{data_columns[index][0]:column for index, column in enumerate(value)} for value in cur1.fetchall()]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(app)
db.init_app(app)

resource_fields = {
    'transaction_id': fields.Integer,
    'price': fields.Integer,
    'date': fields.String,
    'address': fields.String
}

@marshal_with(resource_fields)
@app.route('/')
def data_list():
    return jsonify(data_result)

@marshal_with(resource_fields)
@app.route('/view/<transaction_id>')
def view(transaction_id, methods = ['GET','POST']):
    if request.method == 'GET':
        loan = TransactionsModel.query.filter_by(transaction_id=transaction_id).first()
        if loan:
            cur2 = conn.cursor()
            cur2.execute(f"SELECT * FROM transactions where transaction_id = '{transaction_id}'")
            columns = [column[0] for column in cur2.description]
            results = []
            for row in cur2.fetchall():
                results.append(dict(zip(columns, row)))
            return jsonify(results)
        else:
            return f"Employee with transaction_id = {transaction_id} Does not exist"
    else:
        print('none')

@marshal_with(resource_fields)
@app.route('/add', methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        print("none")
    if request.method == 'POST':
        transaction_id = request.form['transaction_id']
        price = request.form['price']
        date = request.form['date']
        address = request.form['address']
        loan = TransactionsModel(transaction_id=transaction_id, price=price, date=date, address=address)
        db.session.add(loan)
        db.session.commit()
        print(request.form)
        return redirect('/')
    abort(404)

@marshal_with(resource_fields)
@app.route('/update/<transaction_id>',methods = ['GET','POST'])
def update(transaction_id):
    loan = TransactionsModel.query.filter_by(transaction_id=transaction_id).first()
    if request.method == 'GET':
        if not loan:
            return f"Employee with transaction_id = {transaction_id} Does not exist"
    if request.method == 'POST':
        if loan:
            db.session.delete(loan)
            db.session.commit()
            price = request.form['price']
            date = request.form['date']
            address = request.form['address']
            loan = TransactionsModel(transaction_id=transaction_id, price=price, date=date, address=address)
            db.session.add(loan)
            db.session.commit()
            print(transaction_id)
            return redirect(f'/view/{transaction_id}')
        abort(404)
    else:
        print("none")
    return render_template('update.html', loan = loan)

@marshal_with(resource_fields)
@app.route('/delete/<transaction_id>', methods=['GET','POST'])
def delete(transaction_id):
    loan = TransactionsModel.query.filter_by(transaction_id=transaction_id).first()
    if request.method == 'POST':
        if loan:
            db.session.delete(loan)
            db.session.commit()
            return redirect('/')
        abort(404)
    else:
        print("none")
    return render_template('delete.html')

app.run(debug=True)