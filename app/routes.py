""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for, session
from app import app, database as db_helper
import re
import datetime as dt





# 첫 화면, 로그인
@app.route('/', methods=['GET','POST'])
def login():

    msg = ''

    if request.method == 'POST':
        # 접근
        username = request.form['username']
        password = request.form['password']

        # 계정 있는지 확인
        account = db_helper.login_check(username,password)
        # DB에 계정 존재여부 확인
        if account:
            # 세션 정보로 다른 라우트에 접근
            session['loggedin'] = True
            session['id'] = account.id
            session['username'] = account.username
            # 홈페이지로 리다이렉트
            return redirect(url_for('homepage'))
        else:
            # 계정이 없거나 ID/PW 틀렸을때 메시지
            msg = 'Incorrect username or password!'

    return render_template('login.html', msg=msg)


# 로그아웃
@app.route('/logout')
def logout():
    # 세션정보 지우고 로그아웃
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # 로그인 페이지로 리다이렉트
   return redirect(url_for('login'))


# 회원가입
@app.route('/register', methods=['GET', 'POST'])
def register():

    msg = ''

    # 계정 정보 체크
    if request.method == 'POST':
        # 접근
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # 계정 있는지 확인
        account = db_helper.username_check(username)

        # 존재하는 계정에는 에러 메시지 / 유효성 체크
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9가-힣]+', username):
            msg = 'Username must contain only characters and numbers!'
        else:
            # 계정이 존재하지 않고 유효성 통과하면, user 테이블에 새로운 계정 추가

            db_helper.make_account(username, password, email)

            msg = 'You have successfully registered!'

    # 메시지와 함께 등록 폼 보여주기
    return render_template('register.html', msg=msg)


# 회원 정보
@app.route('/profile')
def profile():
    # 사용자가 로그인 했는지 체크
    if 'loggedin' in session:
        # 사용자 정보로 프로필 페이지 보여주기
        account = db_helper.id_check(session['id'])
        return render_template('profile.html', account=account)
    # 로그인 하지 않았을 때는 로그인 페이지로 리다이렉트
    return redirect(url_for('login'))


# 계정 삭제 후
@app.route('/signout')
def signout():
    return render_template('error.html')



# 회원 정보 삭제
@app.route("/delete_all/<username>", methods=['POST'])
def delete_all(username):
    try:
        db_helper.remove_all(username)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


########### CRUD #############


# 게시글 삭제
@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


# 게시글 편집
@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"], data["detail"], data['due_date'], data['user'])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)




# 게시글 생성
@app.route("/create", methods=['POST'])
def create():

    data = request.get_json()
    db_helper.insert_new_task(data['description'], data["detail"], data['due_date'], data['user'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)





# 할일 목록
@app.route("/home")
def homepage():
    if 'loggedin' in session:
        page = request.args.get('page', 1, type=int)
        items = db_helper.fetch_todo(session['username'],page)
        date = dt.datetime.now().strftime('%Y-%m-%d')
        username = session['username']
        return render_template("index.html", items=items, dt=date, user=username)

    return redirect(url_for('login'))






