# MVC Design Pattern(model-view-controller)

장고는 **MTV Pattern(Model Template(view) View(controller))**

흐름은 시험에 나오지 않지만 도움이 된다

![image-20220302125244259](0302_django.assets/image-20220302125244259.png)

## 순서

Django PJT 기본 준비 단계

1. 가상환경 생성 및 활성화 : `python -m venv venv`, `source venv/Scripts/activate`
2. 장고 설치 : `pip install django==3.2` (pip install -r requirements.txt)
3. pip list 작성 : `pip freeze > requirements.txt`
4. **프로젝트 만들기**(설정 폴더) : `django-admin startproject config .` 마지막 .은 현재 폴더에 만든다는 뜻 - **여기만 `django-admin`으로 시작** 나머진 `python manage.py`
5. 서버 실행 : `python manage.py runserver`
6. Application 생성 : `python manage.py startapp articles(앱 이름)`
7. config의 settings.py의 INSTALLED_APPS에 앱 등록
8. 프로젝트 폴더 바로 아래에 'templates'라는 폴더 생성(templates\asfd.html)
9. settings.py에 TEMPLATES에 있는 DIRS 리스트에 'templates' 등록 [BASE_DIR / 'templates']
7. base.html을 생성하고 꾸민다

## 코드 작성 순서

URL -> VIEW -> TEMPLATE

## 프로젝트 구조

지금은 settings.py와 urls.py만 사용

## Application 생성

`python manage.py startapp articles(앱 이름 복수형)`

생성 후 나오는 파일

admin.py, apps.py, models.py, tests.py, views.py

## project vs application 비교

## 앱 등록

config의 settings.py의 INSTALLED_APPS에 앱 등록

## 요청과 응답

path('이정표/', 함수)

view.py - 요청이 오면 실제로 응답하는 파일





## Template

**DTL** (Django Template Language)

https://docs.djangoproject.com/ko/3.2/ref/templates/builtins/

변수 공백일 때 - 1) 오타 2) 값 비어있을 때

**tag** - if나 for 종료 태그 필요

**filter**

forloop.변수들 잘 읽어보기

forloop.counter 등

forloop.counter0

`forloop.counter`The current iteration of the loop (1-indexed)

`forloop.counter0`The current iteration of the loop (0-indexed)

`forloop.revcounter`The number of iterations from the end of the loop (1-indexed)

`forloop.revcounter0`The number of iterations from the end of the loop (0-indexed)

`forloop.first`True if this is the first time through the loop

`forloop.last`True if this is the last time through the loop

`forloop.parentloop`For nested loops, this is the loop surrounding the current one



## language code, time zone

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/seoul'

## 상속

1. 프로젝트 폴더와 같은 위치에 templates폴더 생성
2. 안에 base.html 생성
3. settings.py에서 TEMPALTES에 'DIRS' 에 [BASE_DIR / 'templates'] 추가
4. base.html 작성
5. 각 템플릿 최상단에 {% extends '' %} 추가해서 상속받음
6. 하위 템플릿에서 재지정(overriden) 할 수 있는 블록 작성



## HTML Form

HTTP request method

GET

- 서버로부터 정보를 조회하는 데 사용

- 데이터를 가져올 때만 사용해야함
- Query String Parameter : 주소로 데이터가 전달되는 형태, 주소**?key=value&key1=value&...**
- 데이터 노출되서 중요한 정보는 get으로는 x

/->기본 경로



variable rauting -> dispatcher로 검색