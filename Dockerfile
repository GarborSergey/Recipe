FROM python:3.8.10-alpine

MAINTAINER Robley Gori

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /recipe

WORKDIR /recipe

RUN pip install -r requirements.txt

RUN recipe/manage.py makemigrations

RUN python recipe/manage.py migrate

CMD [ "python", "recipe/manage.py", "runserver", "0.0.0.0:8000" ]