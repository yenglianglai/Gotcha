from GotchaAPP import db
from datetime import datetime

class Fraud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    fraud_label = db.Column(db.Boolean, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "task: {}".format(self.id)