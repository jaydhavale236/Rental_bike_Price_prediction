from calendar import month
from tkinter import Variable
from unittest import result
from networkx import out_degree_centrality
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('Model/Decision.pkl', 'rb'))
    
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
def predict():

    try:
        season = str(request.form["season"])
        holiday = str(request.form["holiday"])
        workingday = str(request.form["workingday"])
        weathersit = str(request.form["weathersit"])
        temp = float(request.form["temp"])
        atemp = float(request.form["atemp"])
        humidity = int(request.form["humidity"])
        windspeed = float(request.form["windspeed"])
        casual = int(request.form["casual"])
        registered = int(request.form["registered"])
        mnth = int(request.form["mnth"])
        year = int(request.form["year"])
        hour = int(request.form["hour"])
        weekday = int(request.form["weekday"])
        
        prediction = model.predict([[season, holiday, workingday, weathersit, temp, atemp, humidity, windspeed, casual, registered, mnth, year, hour, weekday]])
        
        
        
        return render_template("index.html", prediction_text='{}'.format(prediction))
    except Exception as e:
        return jsonify({"error": str(e)})

    
    
