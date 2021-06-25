"""Flask configuration."""


SECRET_KEY = 'your secret key'
SQLALCHEMY_DATABASE_URI = \
    'mysql+pymysql://todolist_my:python123*@192.168.10.71:3306/todolist_my?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

