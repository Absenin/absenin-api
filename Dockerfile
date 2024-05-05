FROM python:3.10.9-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN prisma generate

CMD ["python", "server.py"]