FROM python:3.11.2-slim-bullseye

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

ENTRYPOINT [ "/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "--workers", "4", "labsite.wsgi" ]
