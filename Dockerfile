FROM python:3.10.12-alpine

RUN apk add libstdc++6 libstdc++

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN prisma generate

CMD ["python", "server.py"]