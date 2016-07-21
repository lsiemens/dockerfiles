FROM ubuntu:latest

MAINTAINER Luke Siemens

ENV DEBIAN_FRONTEND noninteractive

EXPOSE 8888

RUN apt-get update && apt-get --no-install-recommends install --yes \
    python2.7 python3 python3-pip git\
    npm nodejs-legacy && \
    npm install -g configurable-http-proxy && \
    apt-get autoremove --yes && apt-get clean all && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade pip && \
    pip3 install setuptools && \
    pip3 install ipython && \
    pip3 install git+git://github.com/jupyterhub/jupyterhub@267994b191fc72fbbaec00b1ad41627e6539fdae && \
    pip3 install notebook
#   install jupyterhub at commit 267994b191fc72fbbaec00b1ad41627e6539fdae because master is unstable and 0.6.1 is too old

COPY jupyterhub-singleuser /usr/local/bin/jupyterhub-singleuser

COPY singleuser.sh /srv/singleuser/singleuser.sh

RUN useradd -d /home/nugrid -m -c "" nugrid && \
    chown -R nugrid:nugrid /home/nugrid && \
    chmod 775 /usr/local/bin/jupyterhub-singleuser && \
    chmod 775 /srv/singleuser/singleuser.sh

USER nugrid

ENV HOME /home/nugrid

WORKDIR /home/nugrid

CMD /bin/bash /srv/singleuser/singleuser.sh
