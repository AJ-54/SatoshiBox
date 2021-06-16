# SatoshiBox

### Overview:
SatoshiBox is a tool for those who want to sell files anonymously and receive BTC or BCH.

### Requirements:
Make sure you have [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) installed. Python version >= 3.6 is required.

You also need Django, django-hitcount and bootstrap-py. These can be installed by running:

```
pip install django
pip install django-hitcount
pip install bootstrap-py
pip install python-dotenv
```
After you have installed the packages mentioned above nativate to your SatoshiBox folder with your terminal and run:
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
Lastly, you can start the server by running:
```
python manage.py runserver 8080
```
