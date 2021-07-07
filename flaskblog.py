from flask import Flask, render_template, url_for, request, session
import requests
import json
app = Flask(__name__)

test = {
"title":"Valorant Go Knife",
"h1":'test1',
"h2":'test2',
"h1": 'test3',
"cars":["Ford", "BMW", "Fiat"]
},{
"title":"Steve",
"p":"steve is a lovely chap",
"age":22,
"cars":["Ferrari", "Merc", "Toyota"]
}

title = 'Home'

@app.route("/")
@app.route("/home")
def home():
    # print(request.args.get('title'))
    return render_template('home.html', posts=test, title=title)

@app.route("/modelling")
def modelling():
    return render_template('modelling.html', test=test)

@app.route("/speechy")
def speechy():
    return render_template('speechy.html', test=test)

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route('/getPost', methods = ['POST'])
def get_post_javascript_data():
    global title
    jsdata = request.form['javascript_data']
    title = jsdata
    return home()

if __name__ == '__main__':
    app.run(debug=True)
