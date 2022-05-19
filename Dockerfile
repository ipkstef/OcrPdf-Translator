FROM python:3.8

COPY ./app/requirements.txt /requirements.txt

COPY ./app/entrypoint.sh /entrypoint.sh

RUN  apt update -y
RUN  apt upgrade -y 
RUN  apt install -y  tesseract-ocr \
    git \
    curl \
    python3-pip \
    ffmpeg\
    libsm6 \
    libxext6 \
    poppler-utils

RUN pip install --upgrade setuptools pip

RUN pip install -r /requirements.txt

EXPOSE 5000
