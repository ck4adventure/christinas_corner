
FROM python:3.12.0-bookworm

# we want a workdir because this ends up in a file system
# just like on a mac, but it's linux alpine
# WORKDIR /code

RUN apt-get update
RUN apt-get install --yes apache2 apache2-dev libapache2-mod-wsgi-py3


# copy and install requirements first to leverage caching
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install mod_wsgi

ENV DJANGO_DEBUG=False

# copy the actual code
COPY . .
RUN python /app/manage.py migrate

EXPOSE 8000


# CMD gunicorn app.wsgi
# CMD gunicorn --chdir /app app.wsgi
CMD mod_wsgi-express start-server /app/app/wsgi.py --user www-data --group www-data
