# HackZurich Refugee Matchmaking
Project to allow refugees to better integrate after relocating.

## Installation
`vagrant up`

## Usage
You can run `vagrant ssh` and then `workon refugee_matchmaking` to start working on the project (which is located in /vagrant).

To run the server, run `python3 manage.py runserver 0.0.0.0:8000`. The admin interface is at [http://localhost:8000/admin](http://localhost:8000/admin), the user and password is `admin`.

## Troubleshooting
You may need to re-install things in virtualenv

**Useful commands:**
```bash
python3 -c "import django; print(django.get_version())"
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```

