from flask import Flask, render_template, url_for
app = Flask(__name__)

test = '<h1>TESTING</h1>'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', test=test)

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
