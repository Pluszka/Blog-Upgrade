from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv()

NPOINT = 'https://api.npoint.io/772691b33e267dc84ebd'

app = Flask(__name__)

articles = requests.get(NPOINT).json()

@app.route('/')
def start():
    return render_template('index.html', posts=articles)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        email_message = f"Subject:New Message\n\nName: {data['your name']}\nEmail: {data['your email']}\nPhone: {data['your phone']}\nMessage:{data['your phone']}"
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login('EMAIL', 'PASSWORD')
        connection.sendmail('EMAIL', 'PASSWORD', email_message)

    return render_template("contact.html")

@app.route('/article/<article_id>')
def article_page(article_id):
    return render_template("post.html", article=articles[int(article_id)-1])


if __name__ == '__main__':
    app.run(debug=True)
