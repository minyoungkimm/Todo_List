"""Defines all the functions related to the database"""
from flask import current_app as app
from app import db
from app.model import User, Task
from werkzeug.security import check_password_hash
import pandas as pd
from sqlalchemy.sql import text


# add: session에 인스턴스를 배치하는데 사용. 그리고 다음 flush 시에 INSERT가 발생
# flush: 트랜젝션을 데이터베이스로 전송합니다. 아직 커밋되지 않은 상태입니다.
# commit: 트랜젝션을 커밋합니다. 내부적으로 항상 flush()를 실행해서 트랜젝션을 flush합니다.


def fetch_todo(username,page) -> dict:


    # result = Task.query.filter(Task.username == username).paginate(page=page, per_page=5)
    idx = 5*(page-1)
    db.session.execute('SET @row_number = {}'.format(idx))
    row_number_column = "(@row_number:=@row_number + 1) AS row_num"
    result = Task.query.filter(Task.username == username
                               ).order_by(Task.id.desc()
                                          ).add_column(text(row_number_column)
                                                       ).paginate(page, per_page=5)


    return result





def update_task_entry(task_id: int, text: str, detail: str ,due: str, user: str):
    """
        주어진 args로 task, detail, due, username 업데이트

        Returns: None
    """
    try:
        result = Task.query.filter(Task.id == task_id).first()
        result.task = text
        result.detail = detail
        result.due = due
        result.username = user
        db.session.commit()
        app.logger.info(f'task update complete! {result}')

    except Exception as e:
        db.session.rollback()
        app.logger.error(e)





def update_status_entry(task_id:int, text: str):
    """
        주어진 args로 status 업데이트

        Returns: None
    """
    try:
        result = Task.query.filter(Task.id == task_id).first()
        result.status = text
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        app.logger.error(e)


def insert_new_task(text:str, detail:str, due:str, user:str):
    """
        새로운 값 추가

        Returns: 새로 추가된 task ID
    """

    try:
        due = pd.to_datetime(due)
        result = Task(task=text, detail=detail, due=due, username=user, status='Todo')
        db.session.add(result)
        db.session.commit()
        app.logger.info(f'task insert complete! username:{user} {result} ')

    except Exception as e:
        db.session.rollback()
        app.logger.error(e)



def remove_task_by_id(task_id: int):
    """ 지우기 """
    try:
        result = Task.query.filter(Task.id == task_id).first()
        db.session.delete(result)
        db.session.commit()
        app.logger.info(f'task delete complete! {result}')

    except Exception as e:
        db.session.rollback()
        app.logger.error(e)





def remove_all(username: str):
    """ 지우기 """
    try:
        result = User.query.filter(User.username == username).first()
        db.session.delete(result)
        db.session.commit()
        app.logger.info(f'account delete complete! {result}')

    except Exception as e:
        db.session.rollback()
        app.logger.error(e)


    # result = Task.query.filter(Task.username == username).all()
    # for res in result:
    #     db.session.delete(res)
    #     db.session.commit()



##################################### 회원 계정 #############################################


def login_check(username:str, password:str):
    result = User.query.filter(User.username == username).first()
    if result and check_password_hash(result.password,password):
        app.logger.info(f'userinfo \n username: {result.username}\n email: {result.email}')
        return result
    return None



def username_check(username:str):
    result = User.query.filter(User.username == username).first()
    # app.logger.info(f'{result} profile check')
    return result



def make_account(username:str, password:str, email:str):
    try:
        result = User(username=username, password=password, email=email)
        db.session.add(result)
        db.session.commit()
        app.logger.info(f'{result} account creation complete!')

    except Exception as e:
        db.session.rollback()
        app.logger.error(e)

