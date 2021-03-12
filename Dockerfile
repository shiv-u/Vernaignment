FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt


RUN mkdir /entity_validation
COPY ./entity_validation /entity_validation
WORKDIR /entity_validation

RUN adduser -D user 

USER user

