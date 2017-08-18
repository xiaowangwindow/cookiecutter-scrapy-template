FROM python:3.5

RUN mkdir -p /usr/src/app
COPY requirements.txt /usr/src/app/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT python -u run.py > run.log
