FROM python:3.7

RUN pip install Flask gunicorn firebase-admin

LABEL maintainer="darthnater007"

COPY src/ /app
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app