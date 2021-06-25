"""Setup at app startup"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


# from app.model import *
# db.create_all()


from app import routes
# route가 별도의 파일에 저장되어 있음을 초기화시 flask에 알려야하기 때문에 마지막줄에 있어야함.




