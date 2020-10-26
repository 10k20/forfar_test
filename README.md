# forfar_test

В папке Server:

1. Установить python 3.6.4
2. Установить virtualenv
3. Создать виртуальную среду (python -m venv venv)
4. Активировать виртуальную средуи (source venv/scripts/activate)
5. Установить все зависимости из requirements.txt (pip install -r requirements.txt)
6. Собрать контейнер (docker build .)
7. Собрать образы Docker (docker-compose up -d --build)
8. Запустить (docker-compose up)
9. Провести миграции (python manage.py makemigrations
                      python manage.py migrage)
10. Создать суперпользователя (python manage.py createsuperuser)
11. Запустить Django (python manage.py runserver)
