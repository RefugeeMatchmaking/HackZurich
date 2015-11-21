# HackZurich Refugee Matchmaking
Project to allow refugees to better integrate after relocating.

## Installation
Navigate to the folder with the vagrant file and run
`vagrant up`
It is usally a good idea to also run
'vagrant provision'

## Usage
SSH into the virtual machine
'vagrant ssh'
The environment is ready for working directly, you just have to set up the database if you don't have one already set up. Then you can run the server with `runserver` or with proper wsgi means.
```bash
You should be in the (refugee_matchmaking) environment here. This is the directory that contains the manage.py script
cd refugee_matchmaking/
python3 manage.py migrate

You'll have to put in a user and password here, for example admin and admin
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```
Now you can visit [http://locahost:8000/admin](http://localhost:8000/admin) and log in with your credentials. 

##Tests
You can test the website by running
python3 manage.py test users 

##NLTK
NLKT database is being used for text matching. You will need to manually download this. Once it has been downloaded you will need to then download the pickle package.
go to `python3`
`import nltk`
`nltk.download()`
download `all`, `punkt`, and `book


## Google App Engine
To open up in your local host while in the directory with play.py and app.yaml
dev_appserver.py --port 8080 .
Note you will need to download the google app engine SDK

To Host the website on appserver.com
appcfg.py -A refugee-lighthouse update app.yaml
