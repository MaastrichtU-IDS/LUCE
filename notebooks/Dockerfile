FROM jupyter/base-notebook

USER root


RUN apt update && \
    apt install -y gcc
    
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /home/jovyan/work