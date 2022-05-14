FROM alpine:3.14

RUN apk update

RUN apk upgrade

RUN apk add tesseract-ocr

RUN apk add git 

RUN apk add curl

COPY ./app/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt


ENTRYPOINT ["python /app/app.py"]

