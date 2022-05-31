from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import joblib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
clf = joblib.load('./model.sav')

from GotchaAPP import routes