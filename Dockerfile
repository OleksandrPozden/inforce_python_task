FROM python:3.8.9

RUN mkdir /app
COPY . /app
COPY requirements.txt /app
RUN python3 -m pip install -r /app/requirements.txt

WORKDIR /app/api