release: python manage.py migrate && python manage.py loaddata bands.json && python manage.py loaddata albums.json
web: gunicorn djangoherokuapp.wsgi