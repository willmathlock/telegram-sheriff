FROM python:3.8.3-alpine

run apk add python3-dev libffi-dev libsodium-dev g++ make gcc libressl-dev musl-dev openssl-dev 

COPY requirements.txt /

RUN pip3 install -r requirements.txt
