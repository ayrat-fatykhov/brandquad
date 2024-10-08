# Тестовое задание

## Задание
Разработать Django приложение для обработки и агрегации Nginx лога.
В составе приложения должна быть Management command, которая на вход принимает ссылку на лог файл определенного формата,
парсит и записывает в БД. Ссылка на файл для теста 
https://drive.google.com/file/d/18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp/view?usp=sharin]. В приложении должна быть модель, 
которая описывает распарсенные данные из лога. Поля модели должны содержать минимум: IP адрес, Дата из лога, http метод
(GET, POST,...), URI запроса, Код ответов, Размер ответа. Учитывать что размер файла может быть до 1Gb. Другие данные из
лога - опциональны. Отображение загруженых данных реализовать через Django admin и API (DRF).

## Запуск проекта
- Клонировать репозиторий
- Активировать виртуальное окружение (команда в терминале: source env/bin/activate)
- Установить зависимости (pip3 install -r requirements.txt)
- Создать файл .env, заполнить его данными из файла .env.sample
- Создать базу данных в postresql
- Создать (python manage.py makemigrations) и применить миграции (python3 manage.py migrate)
- Создать суперпользователя (python3 manage.py csu)
- Загрузить данные в базу данных (python3 manage.py fill)
- Запустить проект "python manage.py runserver"

## Документация к API
- http://127.0.0.1:8000/ (получить список логов, GET)
- http://127.0.0.1:8000/log/view/pk (получить информация о конкретном логе, GET, pk - порядковый номер лога)
