FROM python:3.11.1-alpine3.17

RUN apk update && apk upgrade && apk add bash

WORKDIR /usr/src/app
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

# RUN python manage.py makemigrations \ 
#     && python manage.py migrate 

EXPOSE 80

# CMD gunicorn youtube_api_project.wsgi:application --bind 0.0.0.0:80