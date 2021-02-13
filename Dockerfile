FROM python:3.8.7-alpine

WORKDIR /work

COPY requirements.txt ./

RUN apk add --no-cache --virtual .deps build-base libffi-dev &&\
    python -m pip install -r requirements.txt &&\
    apk del .deps

COPY discordbot.py ./
COPY script ./script

CMD [ "python", "discordbot.py" ]