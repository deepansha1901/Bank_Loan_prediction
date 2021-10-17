# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:59:42 2021

@author: new
"""

from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__,template_folder="templates")
model = pickle.load(open('loan_approval_decision_tree_classifier.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Loan_Amount_Term=360.0
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        Married = int(request.form['Married'])
        Dependents=int(request.form['dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        Loan_Amount = float(request.form['Loan_Amount'])
        Credit_History = float(request.form['Credit_History'])
        Propert_Area = int(request.form['Property_Area'])
        prediction=model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_Amount,Loan_Amount_Term,Credit_History,Propert_Area]])
        output=prediction[0]
        print(output)
        if output==0:
            return render_template('index.html',prediction_text="Your loan will not be approved")
        else:
            return render_template('index.html',prediction_text="Yor loan can be approved")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()
