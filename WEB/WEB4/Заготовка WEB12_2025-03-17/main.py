from flask import Flask
from flask_restful import Api
from data import db_session


# Создадим вторую версию нашего REST-сервиса.
# После создания flask-приложения в файле Qt6.py
# создадим объект RESTful-API:
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app, catch_all_404s=True)

def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()
