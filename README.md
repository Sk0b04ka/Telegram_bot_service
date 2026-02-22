# LinkTracker Bot

Телеграм-бот — прототип сервиса LinkTracker.
На текущем этапе реализован каркас бота с поддержкой команд:

* `/start`
* `/help`
* обработка неизвестных команд

Проект реализован на Python с использованием `python-telegram-bot` для взаимотействия с Telegram API

---
# 🔑 Как получить Telegram-токен

1. В Telegram найти бота **BotFather** (@BotFather)
2. Написать команду:

```
/start
```

3. Затем:

```
/newbot
```

4. Указать:

   * имя бота
   * username

5. BotFather пришлёт токен вида:

```
123456789:AAH48qYjWFIyMheQqpNfqNxtq7XAWNnif9w
```
либо же можно проделать аналогичные действия через интерактивное меню внутри BotFather

---
# Установка и запуск

## 1. Установить зависимости

Убедитесь, что установлен Poetry:

```bash
poetry --version
```

Если нет:

```bash
pip install poetry
```

Далее:

```bash
poetry install
```


## 2. Добавить токен в .env файл

В корне проекта находится файл:

```
.env.example
```

В нём заменить значение "SECRET TOKEN" на полученный ранее токен бота:

```
TELEGRAM_TOKEN="your_telegram_token"
```


## 3. Запуск бота

```bash
poetry run bot
```

После запуска бот начнёт polling и будет принимать команды в Telegram.

---

# Запуск тестов

```bash
poetry run pytest
```
---
# Архитектура проекта

```
project-bot-service/
│
├── src/
│   ├── __init__.py
│   │
│   ├── main.py               
│   ├── app.py                 
│   ├── config.py              
│   ├── logging_config.py      
│   ├── dispatcher.py        
│   ├── telegram_client.py   
│   │
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── base.py           
│   │   ├── start.py         
│   │   ├── help.py           
│   │   └── unknown.py          
│   │
│   └── repository/
│       ├── __init__.py
│       └── user_repository.py  
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_dispatcher.py
│
├── .env.example
├── .gitignore
├── Dockerfile
├── Makefile
├── pyproject.toml
├── poetry.lock
├── README.md
└── .gitlab-ci.yml
```
