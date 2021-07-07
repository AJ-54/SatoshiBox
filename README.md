### Overview
Website/marketplace to sell files anonymously and receive BTC or BCH.

### Requirements
Make sure you have [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) installed. Python version >= 3.6 is required.

You also need Django, and other dependencies. These can be installed by running:

```
pip install -r requirements.txt 
```
After you have installed the packages mentioned above, update the `SECRET_KEY` [here](https://github.com/cnohall/SatoshiBox/blob/master/satoshi_box/settings.py#L28). The [Secret Key](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key) is required to sign the app, Django will refuse to start if `SECRET_KEY` is not set. This [website](https://miniwebtool.com/django-secret-key-generator/) can be used to generate a unique `SECRET_KEY`. 

The `BLOCKONOMICS_API_KEY`, `EMAIL_HOST_USER`, and `EMAIL_HOST_PASSWORD` should be specified [here](https://github.com/cnohall/SatoshiBox/blob/master/satoshi_box/settings.py#L130-L135), with your own values. If you do not have a `BLOCKONOMICS_API_KEY`, you can obtain one by signing up [here](https://www.blockonomics.co/register#/). 

After you have defined the variables mentioned above, nativate to your FileShop folder with your terminal and run:
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```
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

#### Bounties paid till now
- [20USD](https://www.blockonomics.co/api/tx?txid=1819ca971d992e87df59c237d1916402ce6dbe0d51dd3236c5a6b02164034f70&addr=bc1qhnqgfmma6y00ksw9ktpzvvpqut0sa4d8n7y726) to @vv181 for [PR#4](https://github.com/blockonomics/FileShop/pull/4), [PR#8](https://github.com/blockonomics/FileShop/pull/8) and [PR #10](https://github.com/blockonomics/FileShop/pull/10) 

### BitcoinTalk Discussion Thread
https://bitcointalk.org/index.php?topic=5343726.0    
