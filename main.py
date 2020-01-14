from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "Hi!"

@app.route('/home')
def home():
	return "<h1><a href='/about'>My home</h1>"

@app.route('/about')
def about():
	return "<h1>Raimonds Cipkins</h1>"

@app.route('/about_html')
def about_html():
	return render_template ('about.html')

@app.route('/contact_html')
def contacts_html():
  return render_template('contact.html', phone = "26126216")  


app.run(host='0.0.0.0',port=8020)

if_name_=='_main_'
