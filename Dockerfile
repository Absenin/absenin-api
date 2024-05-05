FROM python:3.10.9-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN prisma generate

CMD ["python", "server.py"]