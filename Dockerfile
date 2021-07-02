FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install mysqlclient  

RUN pip install -r requirements.txt

RUN apk del build-deps

COPY . .

EXPOSE 8000

