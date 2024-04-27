from flask import Flask,request, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    return render_template('home.html',pred='You salary prediction will be {}'.format(100000))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    # data = request.get_json(force=True)
    # data_unseen = pd.DataFrame([data])
    # prediction = predict_model(model, data=data_unseen)
    # output = prediction.Label[0]
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)
    
    