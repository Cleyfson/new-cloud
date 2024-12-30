FROM python:3.9-slim

WORKDIR /app

COPY ./api_server /app

RUN pip install --no-cache-dir Flask

EXPOSE 52011

CMD ["python", "app.py"]
