FROM python:3.8-slim

RUN apt-get update && apt-get install -y gcc gettext libgettextpo-dev default-libmysqlclient-dev netcat

ENV PYTHONUNBUFFERED 1

RUN mkdir /app/
WORKDIR /app/

# Probably needed for pillow/tiff support
# RUN apt-get update && apt-get install -y \
#        python-dev python-pip python-setuptools python-tiff \
#        libffi-dev libxml2-dev libxslt1-dev \
#        libtiff-dev libjpeg-dev zlib1g-dev libfreetype6-dev \
#        liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Force reinstall fixes an old bug
# RUN pip3 install pillow --upgrade --force-reinstall --no-cache-dir
