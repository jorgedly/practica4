import os
from flask import Flask, request, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about',)
def about():
    return render_template('about.html')

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000, debug=True)