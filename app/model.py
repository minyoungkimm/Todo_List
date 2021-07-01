from werkzeug.security import generate_password_hash
from app import db



class User(db.Model):
    __tablename__ = 'user'
    # id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), primary_key=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(45), nullable=False)

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.set_password(password)
        self.email = email

    def set_password(self, password):
        self.password = generate_password_hash(password)




class Task(db.Model):
    __tablename__ = 'task1'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)
    due = db.Column(db.DateTime)
    # detail = db.Column(db.String(45))
    detail = db.Column(db.Text)
    username = db.Column(db.String(45), db.ForeignKey('user.username'), nullable=False)

    def __init__(self, task=None, status=None, due=None, detail=None, username=None):
        self.task = task
        self.status = status
        self.due = due
        self.detail = detail
        self.username = username



