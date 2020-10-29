release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py loaddata myfixtures.json
release: python manage.py loaddata fixtures.json
web: gunicorn animal_shelter.wsgi