release: python webplayground/manage.py collectstatic --noinput
web: gunicorn --chdir webplayground webplayground.wsgi --log-file -
