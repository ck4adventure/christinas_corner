
FROM python:3.12.0-alpine

# we want a workdir because this ends up in a file system
# just like on a mac, but it's linux alpine
WORKDIR /code


# copy and install requirements first to leverage caching
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV DJANGO_DEBUG=False

# copy the actual code
COPY . .
EXPOSE 8000

CMD gunicorn app.wsgi