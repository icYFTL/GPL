FROM python:3.7-alpine as gpl
EXPOSE 7865

RUN mkdir /opt/app
WORKDIR /opt/app

COPY source/ ./source/
COPY core.py .
COPY GPL.py .
COPY requirements.txt .
COPY config.json .

RUN pip3 install -r requirements.txt