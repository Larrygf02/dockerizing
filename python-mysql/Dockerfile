FROM python:3.6-slim

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD ./src /app

CMD ["python", "-u", "-m", "start"]