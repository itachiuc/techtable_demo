from flask import Flask , render_template , flash , request , url_for 
import numpy as np 
import pandas as pandas
import re 
import os 
import json

app = Flask(__name__)

global course,details

f = open('courses.json','r')

data = json.load(f)

@app.route('/',methods=['GET','POST']) #flask decorator
def home():
	return render_template("home.html")

@app.route('/android',methods=['GET','POST'])
def android_overview():
	course = data['courses']['android']['name']
	details="Android Development"

	return render_template("home.html",course=course,details=details)
	

if __name__ == '__main__':
	app.run(debug=True)