import json

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = ("WARNING: This is a development server. Do not use it in a production deployment. "
                            "Use a production WSGI server instead.")
params = {'title': 'Home',
          'username': 'Tim',
          "number": 1501}


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", **params)


@app.route('/odd_even')
def odd_even():
    return render_template("odd_even.html", **params)


@app.route('/news')
def news():
    with open("files/news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads((f.read()))
    return render_template("news.html", **params, news=news_list)


if __name__ == "__main__":
    print("http://127.0.0.1:8080/index")
    print("http://127.0.0.1:8080/odd_even")
    print("http://127.0.0.1:8080/news")
    app.run(port=8080, host='127.0.0.1')
