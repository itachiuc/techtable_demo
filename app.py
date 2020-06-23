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
	return render_template("tech.html")

@app.route('/login',methods=['GET','POST']) #flask decorator
def login():
	return render_template("login.html")

@app.route('/course/<course_name>',methods=['GET','POST'])
def overview(course_name):
	title = course_name
	course = data['courses'][course_name]['name']
	tagline = data['courses'][course_name]['tagline']
	related = data['courses'][course_name]['related']
	related_tag = data['courses'][course_name]['related_tag']
	faq = data['courses'][course_name]['faq']
	contents = data['courses'][course_name]['contents']
	length = len(contents)
	inner_contents = data['courses'][course_name]['inner_contents']
	# print(details)
	# print(contents)
	# print(faq)

	return render_template("courses.html",course=course,tagline=tagline,title=title,related=related,related_tag=related_tag,faq=faq,contents=contents,length=length,inner_contents=inner_contents)
	

if __name__ == '__main__':
	app.run(debug=True)