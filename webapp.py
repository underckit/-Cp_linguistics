from flask_pymongo import PyMongo
from flask import render_template, json, request
from flask import jsonify, send_from_directory
import flask
from dbconfig import TABLE_NAME, DATABASE_NAME



app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/v102news")
db = mongodb_client.db



@app.route('/')
def main():
    news = db.news
    return render_template('index.html', news=list(news.find({})))


if __name__ == '__main__':
    app.run(debug=True)


