FROM ubuntu:latest

MAINTAINER Luke Siemens

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get --no-install-recommends install --yes \
    python3 python3-pip \
    npm nodejs-legacy && \
    npm install -g configurable-http-proxy && \
    apt-get autoremove --yes && apt-get clean all && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade pip && \
    pip3 install setuptools && \
    pip3 install jupyterhub oauthenticator dockerspawner

COPY ./jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
COPY ./SSL/ssl.key ./SSL/ssl.crt /srv/jupyterhub/SSL/
RUN chmod 700 /srv/jupyterhub/SSL && \
    chmod 600 /srv/jupyterhub/SSL/*

EXPOSE 8000
