from flask import Flask, render_template
import requests

NPOINT = 'https://api.npoint.io/772691b33e267dc84ebd'

app = Flask(__name__)

aricles = requests.get(NPOINT).json()

@app.route('/')
def start():
    return render_template('index.html', posts=aricles)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
