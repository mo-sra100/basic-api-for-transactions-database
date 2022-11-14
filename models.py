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