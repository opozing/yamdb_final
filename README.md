# YaMDB
### Описание
Благодаря этому проекту можно оценивать фильмы, делиться впечатлениями от просмотра и коментировать записи.
### Технологии
Python 3.7
Django 3.0.5
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
docker-compose up
```
- После создания образа и запуска контейнера выполните команды в терминале:
```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

### Авторы
Сергей