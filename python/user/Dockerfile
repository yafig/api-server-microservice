from python:3.8-slim

WORKDIR /app
RUN apt-get update && apt-get install -qy \
    build-essential python3-dev default-libmysqlclient-dev
    
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD flask run --host 0.0.0.0
