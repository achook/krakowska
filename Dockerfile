FROM python:3.9-alpine

RUN apk update
RUN apk add tzdata
RUN apk add cronie

ENV TZ=Europe/Warsaw

WORKDIR /kielba

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod a+x ./entrypoint.sh

CMD [ "./entrypoint.sh" ]
