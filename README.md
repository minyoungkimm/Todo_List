#### 플라스크 서버 실행하기

1. 가상환경 활성화

   ```shell
   > cd venv/Scripts
   > activate
   ```

2. 의존성 설치

   ```shell
   > cd/path/to/flask-gcp-mysql-demo
   > pip requirement.txt
   ```

3. 환경변수 설정

   ```shell
   > set FLASK_APP=app 
   > set FLASK_DEBUG=1
   > set FLASK_ENV=development
   ```

   > `FLASK_DEBUG` 는 FLASK 어플리케이션에 디버그 모드를 활성화 하여 문제가 발생한 경우 어떤 문제가 발생했는지 자세히 알려준다. 또한 어플리케이션 코드가 변경되었을 때, 자동으로 FLASK서버를 재시작하여 매번 서버를 재시작 해야 하는 수고를 덜어준다.

   

4. 실행

   ```shell
   > flask run
   ```







#### 파일구조

```
TODO_LIST
├── app/
│   ├── static/
│   │   ├── script/
│   │   │   └── model.js
│   │   ├── styles/
│   │   │   ├── custom.css
|   |   |   └── style.css
│   │   └── img
│   │
│   ├── templates/
|   |   ├── index.html
|   |   ├── layout.html
|   |   ├── login.html
|   |   ├── register.html
|   |   ├── profile.html
│   │   └── error.html
│   │
│   ├── __init__.py 
|   ├── routes.py
│   ├── database.py
│   ├── model.py
│   └── config.py
│
└── app.py    # 앱 실행
```



- **`app.py`** :	Flask 서버를 실행
- **`__init__.py`** :	from app import app을 통해서 실행되는 모든 파일들을 전체적으로 초기화 및 실행
- **`route.py`** :	웹 서버로 접근 시 해당 주소로 입력을 하게 되면 특정 함수가 실행되게 도와줌. 프론트엔드의 js를 백엔드 URL에 연결. 
- **`model.py`** :	사용할 모델 생성(User, Task). 속성 지정
- **`database.py`** :	DB와 관련된 모든 함수들 정의(ORM)
- **`config.py`** :	DB접속 정보 및 로깅 정보

