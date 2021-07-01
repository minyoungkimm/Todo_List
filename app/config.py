"""Flask configuration."""
from pathlib import Path


# SECRET_KEY = 'your secret key'
# SQLALCHEMY_DATABASE_URI = \
#     'mysql+pymysql://todolist_my:python123*@192.168.10.71:3306/todolist_my?charset=utf8'
# SQLALCHEMY_TRACK_MODIFICATIONS = False



class Config(object):
    # BASE_DIR = Path().absolute()
    LOG_DIR = './app/logs'
    LOGGER = {
        'version': 1,
        'formatters': {
            'default':{
                'format': '[%(asctime)s] %(levelname)s in %(filename)s %(lineno)s: %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'default'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.StreamHandler',
                'filename': f'{LOG_DIR}/todo.log',
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 5,
                'formatter': 'default',
            },
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }


class DevConfig(Config):
    pass

class ProductionConfig(Config):
    DEBUG = False