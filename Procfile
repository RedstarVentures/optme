web: gunicorn_django -b 0.0.0.0:$PORT -w 9 -k gevent --max-requests 250 --preload optme_test/settings.py

web python optme_test/manage.py runserver 0.0.0.0:$PORT --noreload