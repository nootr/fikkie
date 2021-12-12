FROM python:3.10-alpine

RUN mkdir -p /tmp/broker/out
RUN mkdir -p /tmp/broker/processed

WORKDIR /woof

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY woof/ .

CMD ["celery", "-A", "main", "worker", "-B", "-l", "info"]
