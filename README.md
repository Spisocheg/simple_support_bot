# SimpleSupportBot: Telegram-bot для упрощенной коммуникации клиент-компания

Этот бот упрощает общение между пользователем и администратором компании. Пользователь отправляет свою проблему или вопрос в чат с ботом, а бот пересылает это сообщение администратору. В ответ администратор отправляет совет или решение, которое возвращается пользователю через бота. Удобное решение для поддержки пользователей или личных консультаций.

## Требования

- [Python](https://www.python.org/downloads/) >= 3.10
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) >= 4.26.0
- [python-dotenv](https://github.com/theskumar/python-dotenv) >= 1.0.1 

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/spisocheg/simple_support_bot.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd simple_support_bot
   ```

## Настройка и первый запуск

1. Создайте файл `.env` в корневой директории проекта и добавьте в него следующие переменные окружения (скопируйте из текста ниже):
   ```env
   # Токен бота, получить который можно у @BotFather
   TOKEN=токен_вашего_бота

   # ID Админа, на кого будут отправляться сообщения
   ADMIN_ID=айди_админа

   # Путь к файлу с текстовыми заготовками для бота
   COMMANDS_PATH=src/commands.json
   ```
2. Создайте виртуальное окружение. В корне проекта введите следующее:
   ```bash
   ... > python -m venv venv
   ```
3. После некоторой загрузки в корне проекта появится новая папка (с именем venv). Активируйте виртуальное окружение:
   ```bash
   ... > .\venv\Scripts\activate
   ```
4. В начале строки добавится имя виртуального окружения в скобках. Установите требуемые для работы библиотеки:
   ```bash
   (venv) ... > python -m pip install -r .\requirements.txt
   ```
5. После установки пакетов можете перейти к запуску:
   ```bash
   (venv) ... > python bot.py
   ```
   *консоль не должна ничего выводить

## Использование

### Запуск
1. Перейдите в папку с проектом. Активируйте виртуальное окружение:
   ```bash
   ... > .\venv\Scripts\activate
   ```
2. В начале строки добавится имя виртуального окружения в скобках. Запустите бота:
   ```bash
   (venv) ... > python bot.py
   ```

### Пример использования
Бот принимает стандартные команды: /start, /help, /info
```text
User: /help
Bot: Пишите любое текстовое сообщение, а я перешлю его администратору. Как только он ответит на Ваш вопрос, я сразу же Вам перешлю ответ администратора.
```

## Функциональность

- [x] Отправка сообщений с помощью копирования сообщений
- [x] Отправка сообщений с помощью пересылки сообщений
- [ ] Подключение базы данных для обеспечения анонимности и большей устойчивости функции на основе переслыки

## Структура проекта

```
simple_support_bot/
├── bot.py              # Основной файл бота
├── config.py           # Настройки проекта
├── handlers/           # Обработчики команд
    ├── default.py      # Стандартные команды (/start, /help, /info и все нетекстовые сообщения)
    └── main.py         # Функции обработки текста
├── src/                # Хранилище статических документов
    └── commands.json   # Файл с перечислением всех возможных реплик бота
├── requirements.txt    # Зависимости проекта
└── README.md           # Документация
```

---

Если есть вопросы, пишите: https://t.me/Spisocheg