FROM python:3.8

COPY ./app/requirements.txt /requirements.txt

RUN  apt update -y
RUN  apt upgrade -y 
RUN  apt install -y  tesseract-ocr \
    git \
    curl \
    python3-pip 

RUN pip install --upgrade setuptools pip

RUN pip install translators

RUN pip install -r /requirements.txt