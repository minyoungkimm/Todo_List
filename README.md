### FLASK

- `framework`란? 

  \- 목적에 따라 효율적으로 구조를 짜놓은 개발 방식

  \-  특정 프로그램을 개발하기 위한 여러 요소들과 매뉴얼인 룰을 제공하는 프로그램

- `library`란?

  \- 소프트웨어를 개발하기 쉽게 어떤 기능을 제공하는 도구

- `python`기반 `web framework`

  1.  **Django**

     \- 파이썬 기반 웹프레임워크중 가장 많이 사용됨

     \- 기능이 많고 강력함. MVT기반 패턴대로 개발할 수 있도록 이미 구조화 되어 있어서 가이드 대로 하면 손쉽게 개발이 가능. ORM기능도 내장되어 있으며 MySQL, Oracle 등 다양한 DBMS에 대해서도 Driver형태로 손쉽게 붙일 수 있음

  2. **Flask**

     \- 매우 가볍고 심플한 프레임워크를 지향. 내가 원하는 라이브러리와 패키지로 내가 필요한 것만 붙여서 만들어 나갈 수 있음

     \- Django MVT패턴과 달리 Flask는 보다 일반적인 MVC패턴을 따름

     \- 처음부터 주어진 기능이 없지만, 내가 원하는 설계 방향대로 프레임워크를 구축해 나갈 수 있음

     \- DB ORM구조가 따로 존재하지 않음. 개발자가 원한다면 ORM 지원 패키지를 선택해서 사용하면 됨 (보통 SQLAlchemy 사용)





- `ORM`

  \- 데이터베이스와 객체지향 프로그래밍 언어간의 호환되지 않은 데이터를 변환하는 프로그래밍 기법.

  \- SQLAlchemy는 python을 위한 ORM중에 하나로 DBMS의 테이블을 하나의 객체로 보고 객체간의 관계를 프로그래밍 언어로 풀어냄

  \- 파이썬 객체(Class)에 데이터 모델(Model)을 정의해서 파이썬에서 만든 데이터 모델 객체와 데이터베이스를 연결시켜준다.

  \- **장점 **: 

  1) ORM을 이용하면 따로 SQL문을 짤 필요없이 객체를 통해 간접적으로 데이터베이스를 조작할 수 있음. 직관적인 관계 파악이 가능

  2) 데이터 구조 변경시 객체에 대한 변경만 이루어지면 되므로 유지보수성이 좋다.

  3) 객체를 통하여 대부분의 데이터를 접근 및 수정하므로, 코드가독성이 좋다.

  \- **단점** :

  1) 복잡한 쿼리 작성시, ORM 사용에 대한 난이도가 급격히 증가한다.

  2) 호출 방식에 따라 성능차이가 크다

  3) DBMS 고유의 기능을 전부 사용하지는 못한다.





- `MVC`패턴

  1. **Model**

     \- "무엇"을 할지를 정의. 내부 로직을 처리하기 위한 역할

     \- 처리되는 알고리즘, DB와 상호작용(CRUD), 데이터 등등

  2. **Controller**

     \- 모델이 "어떻게" 처리할 지를 알려주는 역할. 화면 로직처리 부분

     \- 화면에서 사용자의 요청을 받아서 처리되는 부분을 구현하게 되며, 요청 내용을 분석해서 Model과 View에 업데이트 요청을 함

     \- 사용자로부터 입력을 받고 *Model 또는 View 중개인 역할* . API로직을 담당

  3. **View**

     \- 화면에 "무엇" 인가를 "보여주기 위한 역할"

     \- 컨트롤러 하위에 종속되어, 모델이나 컨트롤러가 보여주려고 하는 모든 필요한 것들을 보여줌

     \- 최종 사용자에게 "무엇"을 화면(UI)으로 보여줌
     
     \- 클라이언트에서 넘어온 request를 처리하는 route 매서드로 인터페이스를 처리



- `blueprint`

  Flask 는 application component를 만들거나, application 안팎으로 공통적인 패턴을 지원하는 목적으로 블루프린트라는 컨셉을 사용한다.

  블루프린트는 큰 application을 단순화시키는 역할을 하고, Flask extension(확장 프로그램, 라이브러리 등) 등록을 위한 중심 수단으로 쓰인다.

  <hr>

  플라스크는 django와 달리 url들을 파일 단위에서 따로 관리하지 않고, controller에 endpoint함수에 데코레이터를 붙여서 관리한다.

  라우트함수들을 기능이 필요할 때마다 계속 추가되어야 하기 때문에, create_app함수 내에 함수가 많을 경우 번거로워질 수 있다.

  이런 상황에서 블루프린트를 이용하면 라우트 함수들을 보다 구조적으로 관리할 수 있게 된다.

  <hr>
  
  flask 에서 blueprint 라는 것을 제공한다. 쉽게 풀어서 이야기하면, module 을 url 에 등록하기 쉽게 해주는 방법이다.
  
  만약 당신이 url 에 특정 handler 를 mapping시키는데, 그 url mapping 하는 곳은 보통 application 에서 한 곳에 집중되어 있다. 이 부분을 각 module 같은 단위 요소로 나눠놨을 때 이 녀석들을 손쉽게 중앙의 url dispatcher 에 등록시킬 수 있도록 해놓는 것이 blueprint 라고 생각하면 될 듯 하다.
  
  
  
  
  
  











#### 플라스크 서버 실행하기

1.  가상환경 활성화

   ```shell
   > cd venv/Scripts
   > activate
   ```

2.  의존성 설치

   ```shell
   > cd/path/to/flask-gcp-mysql-demo
   > pip requirement.txt
   ```

3.  환경변수 설정

   ```shell
   > set FLASK_APP=app 
   > set FLASK_DEBUG=1
   > set FLASK_ENV=development
   ```

   > `FLASK_DEBUG` 는 FLASK 어플리케이션에 디버그 모드를 활성화 하여 문제가 발생한 경우 어떤 문제가 발생했는지 자세히 알려준다. 또한 어플리케이션 코드가 변경되었을 때, 자동으로 FLASK서버를 재시작하여 매번 서버를 재시작 해야 하는 수고를 덜어준다.

   

4.  실행

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
- **`config.py`** :	DB접속 정보



#### 데이터 베이스 (Mysql)

클라이언트가 서버에 요청을 보냄   >>   서버가 데이터 베이스에 쿼리를 보냄   >>   데이터베이스가 데이터를 반환함   >>   서버가 html을 렌더링   >>   최종 html을 클라이언트에게 프론트 엔드로 제공





![image-20210623161229987](C:\Users\KBet\flask-gcp-mysql-demo\image-20210623161229987.png)







#### API(Application Programming Interface)

API는 컴퓨터나 시스템과 상호작용하여 정보를 검색하거나 기능을 수행하고자 할 때, 사용자가 원하는 것을 시스템에 전달할 수 있게 지원하여 시스템이 이 요청을 이해하고 이행할 수 있도록 해주는 역할. 세션이나 쿠키정보가 필요없음.



#### REST

HTTP URI를 통해 자원을 명시하고, HTTP METHOD를 통해 해당 자원에 대한 CRUD Operation을 적용하는것