
## Описание: 
В рамках проекта реализован многофункциональный API для социальной сети YaTube. Для аутентификации пользователей используются JWT-токены библиотеки Djoser.

#### Возможности API:
Для авторизованных пользователей: 
* Публикация и управление (редактирование, удаление) своими постами;
* Добавление комментариев к постам;
* Возможность просмотра всех постов и комментариев социальной сети;
* Возможность просмотра и управления своими подписками.

Для неавторизованных пользователей: 
* Возможность просмотра всех постов и комментариев социальной сети;

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/farrukhrus/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов: 
По адресу http://127.0.0.1:8000/redoc/ доступна подробная документация для API.

* #### Генерация JWN токена:
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
```
Request body:
```
{
    "username": "regular_user",
    "password": "iWannaBeAdmin"
}
```
Response:
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMDMyOTk2OSwianRpIjoiN2Y4YzMxMTcwN2U5NDNkMWJhNDM2ODczNDI5MTg1NGEiLCJ1c2VyX2lkIjoyfQ.NzDqe8-KCflkjBfI4PoMOiKXGLyBbMtQxqD3lG0Ui2g",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAwMzI5OTY5LCJqdGkiOiJiOTZjYWQ5Y2ZkMjM0NzQ1Yjg2MzM4M2I0MThhYmYxYyIsInVzZXJfaWQiOjJ9.cuEMDl72v-l1zcSMy8-Wt5NZYFLp-YHUr5tgceA0jaQ"
}
```

* #### Создание поста без привязки к группе:
```
POST http://127.0.0.1:8000/api/v1/posts/
```
Request body:
```
{
    "text": "Пост зарегистрированного пользователя."
}
```
Response:
```
{
    "id": 1,
    "text": "Пост зарегистрированного пользователя.",
    "author": "regular_user",
    "pub_date": "2023-11-17T17:53:14.287211Z",
    "image": null,
    "group": null
}
```

* #### Добавления комментария к посту:
```
POST http://127.0.0.1:8000/api/v1/posts/{{id поста}}/comments/
```
Request body:
```
{
    "text": "Тестовый комментарий"
}
```
Response:
```
{
    "id": 1,
    "author": "regular_user",
    "post": 2,
    "text": "Тестовый комментарий",
    "created": "2023-11-17T19:35:17.814877Z"
}
```
