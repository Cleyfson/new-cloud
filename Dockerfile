FROM python:3.9-slim

WORKDIR /app

COPY ./api_server /app

RUN pip install --no-cache-dir Flask

EXPOSE 30502

CMD ["python", "app.py"]
