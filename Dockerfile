FROM python:3.8

COPY ./app/requirements.txt /requirements.txt

RUN sudo apt update -y
RUN sudo apt upgrade -y 
RUN sudo apt install -y  tesseract-ocr \
    git \
    curl \
    py3-pip

RUN pip install --upgrade setuptools pip

RUN pip install -r /requirements.txt


ENTRYPOINT ["python /app/app.py"]

