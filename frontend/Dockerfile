FROM alpine:3.6

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache python3
RUN pip3 install -r /requirements.txt

