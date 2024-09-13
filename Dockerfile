FROM python:3.10-slim-buster AS build

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["fastapi", "run", "src/main.py", "--port", "8000"]