# Старт код проекта с Фреймворком FastAPI с использованием HTML&CSS и MySQL



## Описание
Этот проект представляет собой шаблон для быстрого создания приложения на FastAPI с использованием MySQL в качестве базы данных. Проект включает готовую структуру папок и файлов, что позволяет быстро приступить к разработке.

## Установка

   1. Установка библиотек и фреймворков. [ * ]
	
	```bash
	pip install -r requirements.txt


   2. Создание Виртуальное окружение и его активация.
	
	```bash
	python -m venv venv .\venv\Scripts\activate  # для Windows

## Структура проекта

C:
│   README.txt                   # Этот файл
│   requirements.txt             # Зависимости проекта
│
├───app
│   │   main.py                  # Точка входа в приложение
│   │   models.py                # Модели   
│   │
│   ├───routers				  # Маршруты API
│   │       auth.py
│   │       user.py
│   │
│   ├───static                  # CSS, JS, изображения
│   │       styles.css
│   │
│   └───templates               # HTML шаблоны
│           base.html
│           login.html
│           profile.html
│
└───database                    # Подключение к базе данных и SQL запросы
        connection.py            # Настройка подключения к MySQL
        queries.py               # SQL запросов

## Использование 

1. Запуск сервера FastAPI:

   ```bash
   uvicorn app.main:app --reload

2. Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к API.

3. Для доступа к документации используйте http://localhost:8000/docs или http://localhost:8000/redoc.



### Контакты

Username: ⲙαρτιнеss
Telegram: @OO1111OOO ( O - это o )
Email: zuhnnnkenzy@gmail.com

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной.

 