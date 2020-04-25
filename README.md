# lesson-django

```sh
$ pip install django
$ django-admin startproject config . # アプリケーションの基本構成を立ち上げ
$ python manage.py runserver         # Djangoのサーバを起動してみる
```

### データベースモデルの作成

models.pyを編集した後に

```sh
$ python manage.py makemigrations    # migration定義を作成
$ python manage.py migrate           # データベースに反映を実行する
```

### 管理ユーザの作成
```sh
$ python manage.py createsuperuser

Username: admin
Email address: hoge@huga.com
Password: aiueo1234
Password (again): aiueo1234
```