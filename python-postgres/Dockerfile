FROM python:3.6-slim

WORKDIR /app

RUN apt update -y

RUN apt install -y python3-dev libpq-dev gcc

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD ./src /app

CMD ["python", "-u", "-m", "main"]