
FROM python:3.12.0-slim-bookworm

RUN apt-get update
RUN apt-get install --yes apache2 apache2-dev libapache2-mod-wsgi-py3


# copy and install requirements first to leverage caching
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
RUN pip install mod_wsgi

# ENV DJANGO_DEBUG=False

# copy the actual code
COPY . .
# RUN python /app/manage.py migrate

EXPOSE 8000


# CMD gunicorn app.wsgi
# CMD gunicorn --chdir /app app.wsgi
CMD mod_wsgi start-server wsgi.py --port=8000 \
    --user www-data --group www-data \
    --log-to-terminal
 
#   --server-root=/etc/mod_wsgi-express-80