# HackZurich Refugee Matchmaking
Project to allow refugees to better integrate after relocating.

## Installation
`vagrant up`

## Usage
The environment is ready for working directly, you just have to set up the database if you don't have one already set up. Then you can run the server with `runserver` or with proper wsgi means.
```bash
# You should be in the (refugee_matchmaking) environment here
cd refugee_matchmaking/
python3 manage.py migrate

#You'll have to put in a user and password here, for example admin and admin
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```
Now you can visit [http://locahost:8000/admin](http://localhost:8000/admin) and log in with your credentials. 