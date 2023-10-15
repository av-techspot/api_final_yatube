# YaTubeAPI
![android-chrome-192x192](https://user-images.githubusercontent.com/19632240/224033450-66a55bd2-10a7-40da-85a0-dfefa08549b3.png)


Программный интерфейс для обмена данными с соцсетью **YaTube**

### Стек:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

### Как запустить проект:
- _Клонировать репозиторий и перейти в него в командной строке:_
```
git clone https://github.com/api_final_yatube.git
cd api_final_yatube
```
- _Cоздать и активировать виртуальное окружение:_
```
python3 -m venv env
source env/bin/activate
```
- Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Выполнить миграции:
```
python3 manage.py migrate
```
- Запустить проект:
```
python3 manage.py runserver
```

### Документация
При запуске проекта, документация будет доступна по адресу:
http://127.0.0.1:8000/redoc/#tag/api
