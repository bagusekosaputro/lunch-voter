FROM python:3.10-slim-buster AS build

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000
COPY ./runserver.sh /
RUN chmod +x /runserver.sh
ENTRYPOINT ["/runserver.sh"]