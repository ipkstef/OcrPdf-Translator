FROM alpine:3.14

COPY ./app/requirements.txt /requirements.txt

RUN apk update\
 apk upgrade \
 apk add tesseract-ocr \
 apk add git \
 apk add curl \
 apk add --update py3-pip \
 pip3 install --upgrade setuptools pip \
 pip3 install opencv-python \
 pip install -r /requirements.txt


ENTRYPOINT ["python /app/app.py"]

