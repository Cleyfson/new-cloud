FROM python:3.10-slim

WORKDIR /app

COPY ./rules-generator /app

RUN pip install --no-cache-dir pandas fpgrowth-py

RUN mkdir -p /mnt/project2-pv2-cleifsonaraujo

EXPOSE 5000

CMD ["python", "app.py"]
