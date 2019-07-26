FROM python:latest

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip --no-cache-dir install -r requirements.txt
COPY . .


USER root
RUN chmod a+w ./logs
CMD ["python", "Deployer/app.py"]
