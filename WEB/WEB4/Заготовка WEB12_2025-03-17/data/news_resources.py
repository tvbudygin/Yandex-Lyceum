from flask import jsonify
from flask_restful import abort, Resource
from data import db_session
from data.news import News


def abort_if_news_not_found(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")


class NewsResource(Resource):
    def get(news_id):  # получаем новости при помощи api
        db_sess = db_session.create_session()  # создаем переменную которая поможет перенести данные из бд
        news = db_sess.query(News).get(news_id)
        if not news:
            return jsonify({'error': 'not found'})
        return jsonify(
            {
                'news':
                    news.to_dict(only=('title',
                                       'content',
                                       'user_id',
                                       'is_private'))
            }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': 'ok'})


class NewsListResource(Resource):
    def get(news_id):  # получаем новости при помощи api
        db_sess = db_session.create_session()  # создаем переменную которая поможет перенести данные из бд
        news = db_sess.query(News).get(news_id)
        if not news:
            return jsonify({'error': 'not found'})
        return jsonify(
            {
                'news':
                    news.to_dict(only=('title',
                                       'content',
                                       'user_id',
                                       'is_private'))
            }
        )

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        news = News(
            title=request.json['title'],
            content=request.json['content'],
            user_id=request.json['user_id'],
            is_private=request.json['is_private']
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'id': news.id})