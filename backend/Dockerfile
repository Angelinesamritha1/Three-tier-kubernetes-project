FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask flask-cors mysql-connector-python

EXPOSE 5000

CMD ["python","-u", "app.py"]
