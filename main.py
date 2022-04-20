from flask import Flask, render_template, request
import requests

NPOINT = 'https://api.npoint.io/772691b33e267dc84ebd'

app = Flask(__name__)

articles = requests.get(NPOINT).json()

@app.route('/')
def start():
    return render_template('index.html', posts=articles)

@app.route("/about", methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        data = request.form
        print(data["your name"])
        print(data["your email"])
        print(data["your phone"])
        print(data["your message"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("about.html")


@app.route("/contact" )
def contact():
    return render_template("contact.html")

@app.route('/article/<article_id>')
def article_page(article_id):
    return render_template("post.html", article=articles[int(article_id)-1])
#
# @app.route('/form-entry', methods=['POST', 'GET'])
# def recive():
#     data = request.form
#     print(data["your name"])
#     print(data["your email"])
#     print(data["your phone"])
#     print(data["your message"])
#     return "<h1>Successfully sent your message</h1>"


if __name__ == '__main__':
    app.run(debug=True)
