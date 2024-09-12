FROM python:3.10-slim-buster

WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000
COPY ./runserver.sh /
RUN chmod +x /runserver.sh
ENTRYPOINT ["/runserver.sh"]