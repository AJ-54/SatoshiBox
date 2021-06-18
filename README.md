### Overview
Website/marketplace to sell files anonymously and receive BTC or BCH.

### Requirements
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
### Business Model
Hosting and running the project can be good revenue source. Owner of website can earn revenue by charging commision from sellers while withdraw. Various features/enhancement can be added by any developer to differentiate their marketplace. 

#### Funding
While eventually, the project should be self sustaining, Blockonomics has initially commited to funds of 1000USD in bitcoin to kickstart the development. Funding will be given to merged pull requests classified as following:

- Easy (5-20USD) : Minor changes in UI/styling, few line bug fixes, documentation 
- Medium (20-100USD): Adding a minor feature that requires 10+ lines of code, substantial frontend functionality
- Hard (100-250USD): A new feature that noticeably increases the project functionality, major refactoring / new UI components 

### BitcoinTalk Discussion Thread
https://bitcointalk.org/index.php?topic=5343726.0    
