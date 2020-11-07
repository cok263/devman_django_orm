# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в
этот репозиторий слуйчайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД,
но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами
и карточками пропуска сотрудников нашего банка.

### Как установить

Файле projects/.env должен содержать информацию для подключения к БД и содержать такие параметры:
- DB_USER(имя пользователя БД)
- DB_PASSWORD(пароль пользователя БД)
- SECRET_KEY(секретный ключ)
- DEBUG(отладочный режим)

Пример .env
```
DB_USER = user
DB_PASSWORD = password
SECRET_KEY = secret_key
DEBUG = false
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Запуск
Проект запускается командой 
```
python manage.py runserver 0.0.0.0:8000.
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).