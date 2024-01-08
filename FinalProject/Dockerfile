FROM tensorflow/tensorflow:latest-gpu

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install sudo -y build-essential \
    python3-pip \
    python3-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN sudo apt install ffmpeg -y
RUN sudo apt-get install espeak -y

RUN apt-get clean

RUN mkdir /src
WORKDIR /src
COPY ./src /src
RUN adduser user
USER user