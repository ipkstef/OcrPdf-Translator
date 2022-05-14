FROM alpine:3.14

RUN apk update

RUN apk upgrade

RUN apk add tesseract-ocr

RUN apk add git 

RUN apk add curl



ENTRYPOINT ["tesseract"]

