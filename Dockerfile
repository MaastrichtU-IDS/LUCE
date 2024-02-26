# FROM jupyter/base-notebook:python-3.7.6
# FROM continuumio/miniconda3
FROM python:3.7

USER root
WORKDIR /app

ENV USE_TZ=False

RUN apt update && \
    apt install -y wget build-essential software-properties-common libssl-dev  postgresql-client libpq-dev


# Install Ethereum
# RUN add-apt-repository -y ppa:ethereum/ethereum && \
#     apt update && \
#     apt install -y ethereum


# Install from requirements.txt to only rebuild when requirements file change
ADD requirements.txt .

RUN pip install -r requirements.txt

COPY scripts/entrypoint.sh /entrypoint.sh



COPY . .

RUN pip install -e .

RUN python -m solcx.install v0.4.25




EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]