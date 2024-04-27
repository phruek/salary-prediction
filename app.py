print("test")

from flask import Flask,request, url_for, redirect, render_template, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)