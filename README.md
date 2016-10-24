# HackUPC Live API

## Development

Required: python 3.4.3, pip, virtualenv

### Prepare

- Setup python virtualenv and activate
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py createsuperuser`

### Run server

- `python manage.py runserver localhost:8000`
- Open browser at [localhost:8000](http://localhost:8000)

### Create events
- Run server
- Log in with credentials
- Open browser at [localhost:8000/events/](http://localhost:8000/events/)
- Use form to send a *POST* request


-----------

Made with <3 in Barcelona by [casassg](http://gerard.space)