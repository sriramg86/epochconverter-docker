FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install -y python3.5 python3-pip

RUN pip3 install flask

RUN pip3 install wtforms

COPY epochtime.py /opt/epochtime.py

ADD static /opt/static

ADD templates /opt/templates
 
ENTRYPOINT python3 /opt/epochtime.py