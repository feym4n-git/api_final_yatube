Описание проекта Yatube API:

Это API для социальной сети для публикации личных дневников.

Примеры запросов:

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/feym4n-git/api_final_yatube
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

Примеры запросов:

  /api/v1/posts/:
    get:
      operationId: Получение публикаций
      description: >-
        Получить список всех публикаций. При указании параметров limit и offset
        выдача должна работать с пагинацией.
	{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

	[

        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]

	}
            
    post:
      operationId: Создание публикации
      description: >-
        Добавление новой публикации в коллекцию публикаций. Анонимные запросы
        запрещены.
      parameters: 
				{
				"text": "string",
				"image": "string",
				"group": 0
				}
				
После запуска проекта по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. Документация представлена в формате Redoc.

Автор: Dmitriy Zemtsov Contacts: dmitriyzemtsov@yandex.ru
