FROM python:3.10.4-alpine3.15

COPY ./app/requirements.txt /requirements.txt

RUN apk update
RUN apk upgrade 
RUN apk add tesseract-ocr \
    git \
    curl \
    py3-pip

RUN pip install --upgrade setuptools pip

RUN pip install opencv-python

RUN pip install -r /requirements.txt


ENTRYPOINT ["python /app/app.py"]

