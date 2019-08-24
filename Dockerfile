FROM python:latest

ARG GIT_USERNAME
ARG GIT_PASSWORD

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
COPY . .


USER root
RUN chmod a+w ./logs
RUN mkdir -p /opt/services
RUN apt-get update
RUN apt-get --assume-yes install vim docker-compose

ENV GIT_USERNAME=$GIT_USERNAME
ENV GIT_PASSWORD=$GIT_PASSWORD

CMD ["python", "Deployer/app.py"]

