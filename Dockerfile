FROM alpine:3.14

COPY ./app/requirements.txt /requirements.txt

RUN apk update\
 apk upgrade \
 tesseract-ocr \
 git \
 curl \
 py3-pip 

RUN pip3 install --upgrade setuptools pip
 
RUN PIP3 install opencv-python

RUN pip3 install -r /requirements.txt


ENTRYPOINT ["python /app/app.py"]

