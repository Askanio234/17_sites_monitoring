# Мониторинг сайтов

Скрипт проверяет домены из текстового файла.
Для того что бы пройти проверку сервер должен ответить с кодом 200 и имя должно быть проплачено на более, чем месяц вперед

# Как запустить

Запуск на Linux:
Перед запуском установить зависимости:
```#!bash
pip install -r requirements.txt
```
Один обязательный параметр ```filepath``` - путь до текстового файла с доменами

```#!bash

$ E:\Users\projects\17_sites_monitoring>python check_sites_health.py site_list.txt
https://www.google.com статус - Ok!
https://www.yandex.com статус - Ok!
https://www.tesla.com статус - Ok!
https://learn.python.ru статус - Ok!
https://www.youtube.com статус - Ok!
https://www.alfabank.ru статус - Ok!
https://www.github.com статус - Ok!
https://www.python.org статус - Ok!

```

Запуск на Windows происходит аналогично.

# Цели проекта

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
