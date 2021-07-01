"""Setup at app startup"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

import logging
from logging import handlers
import logging.config
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler





app = Flask(__name__)
app.secret_key = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://todolist_my:python123*@192.168.10.71:3306/todolist_my?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


# logging to file
# 일자별로 파일 따로 저장하기
handler = TimedRotatingFileHandler('./app/logs/todo.log', when='midnight', interval=1, encoding='utf-8',backupCount=10)
handler.suffix = "%Y%m%d"
# handler = RotatingFileHandler('./app/logs/todo.log', maxBytes=1024 * 1024, backupCount=10)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(filename)s %(lineno)s: %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# app.config.from_object(os.environ['APP_SETTINGS'])
# logging.config.dictConfig(app.config['LOGGER'])





from app import routes
# route가 별도의 파일에 저장되어 있음을 초기화시 flask에 알려야하기 때문에 마지막줄에 있어야함.




