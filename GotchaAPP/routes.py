import pandas as pd
import numpy as np
from flask import render_template, request
from GotchaAPP import db, clf, app
from GotchaAPP.model import Fraud



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = pd.read_csv(request.files['fileupload'], index_col=[0])
        X = data.drop(columns=['fraud_ind']).iloc[:100]
        X_test = data.drop(columns=['fraud_ind', 'cano', 'conam']).iloc[:100]
        X_predict = clf.predict(X_test)
        fraud_index = np.where(X_predict == 1)[0].tolist()

        count = 0
        for index, case in X.iterrows():
            if(count in fraud_index):
                new_case = Fraud(
                    bank_id=case['cano'], amount=case['conam'], fraud_label=True)
            else:
                new_case = Fraud(
                    bank_id=case['cano'], amount=case['conam'], fraud_label=False)
            try:
                db.session.add(new_case)
                db.session.commit()
            except:
                return 'There was an issue adding your task'
            count += 1

        fraud_case = Fraud.query.order_by(Fraud.date_created).all()
        return render_template('result.html', fraud_case=fraud_case)