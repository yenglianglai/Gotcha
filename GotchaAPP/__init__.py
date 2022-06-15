from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import joblib
import sklearn
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

maps = {
    "Country": {
        "104": "Taiwan",
        "38": "Spain",
        "46": "Japan",
        "75": "Korea",
        "102": "India",
        "52": "Brazil"
    },
    "Coin": {
        "62": "NTD",
        "61": "USD",
        "60": "JPY",
        "71": "Russian Ruble",
        "26": "RMB"
    },
    "Store": {
        "54238.0": "s1",
        "54828.0": "s2",
        "55807.0": "s3"
    }
}


class Fraud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cano = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    fraud_label = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "task: {}".format(self.id)


db.create_all()
db.session.commit()

clf = joblib.load('./model.sav')

from GotchaAPP import routes
