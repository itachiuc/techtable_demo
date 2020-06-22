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

@app.route('/course/<course_name>',methods=['GET','POST'])
def overview(course_name):
	title = course_name
	course = data['courses'][course_name]['name']
	details = data['courses'][course_name]['requirements']

	print(details)

	return render_template("home.html",course=course,details=details,title=title)
	

if __name__ == '__main__':
	app.run(debug=True)