release: python manage.py migrate && python manage.py loaddata initialBands.yaml
web: gunicorn djangoherokuapp.wsgi