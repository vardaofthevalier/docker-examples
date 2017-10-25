FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y install python-pip python-dev
RUN mkdir -p /flask/app
COPY app/ /flask/app/
COPY setup.py /flask/setup.py
WORKDIR /flask
RUN pip install -U pip && pip install -U .
WORKDIR /flask/app
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:80", "wsgi"]