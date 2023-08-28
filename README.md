


<h1 align="center">Parser_HH_with_DB</h1>
<h2 align="center">Парсинг вакансий. Работа с базой данных</h2>

<div align="center">
<div>
    <a href="https://docs.pydantic.dev/latest/contributing/#badges" rel="nofollow"><img src="https://pypi-camo.global.ssl.fastly.net/efb81286fc744fbf809859d1089c3c8b100bbfd3/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f707964616e7469632f707964616e7469632f6d61696e2f646f63732f62616467652f76322e6a736f6e" alt="Pydantic v2"></a>
    <a href="https://pypi.org/project/requests/2.29.0/"> <img alt="Static Badge" src="https://img.shields.io/badge/requests-2.29.0-green"></a>
    <a href="https://pypi.org/project/psycopg2/2.9.6/"><img alt="Static Badge" src="https://img.shields.io/badge/psycopg2--binary-2.9.6-green?labelColor=red&color=blue"></a>
</div>
<div>
    <a href="https://www.python.org/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"/></a>
    <a href="https://www.postgresql.org/"><img width="48" height="48" src="https://img.icons8.com/color/48/postgreesql.png" alt="postgreesql"/></a>
</div>
</div>

___
## Задачи
### Закрепить первоначальные знания по темам:
1. Создание БД;
2. Создание таблиц;
3. Базовые SQL-запросы;
4. Продвинутый синтаксис;
5. Data Definition Language;

___
## Установка

1. Откройте проект с помощью Get from VCS.
2. Введите ссылку на удалённый репозиторий. 
```bash
    git@github.com:AndrewDyakonow/Parser_HH_with_DB.git
```
3. Создайте и активируйте виртуальное окружение.
```bash
    python3 -m venv venv
    source venv/bin/activate
```
4. Установите зависимости.
```bash
    pip install -r requirements.txt
```

5. Парсер работает с БД PostgreSQL. Поэтому требуется иметь
установленную СУБД Postgtes. 

Для настройки подключения к БД необходимо внести изменения
в файл database.ini, заменив *** на Ваши данные

```
[postgresql]
host=localhost
port=5432
user=***
password=***

```

___

## Описание

1. При запуске файла main.py необходимо набрать ключевое слово или фразу для поиска и нажать ENTER
2. Если по ключевому слову или фразе вакансий не будет найдено, то выведется соответствующее сообщение
3. После получения вакансий, их можно отсортировать по зарплате, от большей к меньшей
4. Далее автоматически создастся и заполнится база данных по найденным вакансиям
5. В завершении можно выбрать запрос из базы данных для удобного отображения вакансий
6. Обратите внимание, что для запроса № 5 необходимо будет ввести ключевое слово для поиска по названию вакансии
7. В конце необходимо набрать "0", для завершения работы
