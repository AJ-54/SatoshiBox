# SatoshiBox

### Overview:
SatoshiBox is a tool for those who want to sell files anonymously and receive BTC or BCH.

### Requirements:
Make sure you have [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) installed. Python version >= 3.6 is required.

You also need Django, and other dependencies. These can be installed by running:

```
pip install -r requirements.txt 
```
After you have installed the packages mentioned above nativate to your SatoshiBox folder with your terminal and run:
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
Update the `SECRET_KEY` [here](https://github.com/cnohall/SatoshiBox/blob/master/satoshi_box/settings.py#L28) and the `BLOCKONOMICS_KEY`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` [here](https://github.com/cnohall/SatoshiBox/blob/master/satoshi_box/settings.py#L130-L135), with your own values. If you haven't yet set up [Blockonomics Xpub merchant](https://www.blockonomics.co/merchants#/) value, please set it up first. It is recommended that you do so by specifying your own `.env` file. 
Lastly, you can start the server by running:
```
python manage.py runserver 8080
```
