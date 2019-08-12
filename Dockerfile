FROM python:latest

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip --no-cache-dir install -r requirements.txt
COPY . .


USER root
RUN chmod a+w ./logs
RUN mkdir -p /opt/services

ENV GIT_USERNAME=$GIT_USERNAME
ENV GIT_PASSWORD=$GIT_PASSWORD

CMD ["python", "Deployer/app.py"]

