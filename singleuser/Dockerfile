FROM ubuntu:latest

MAINTAINER Luke Siemens

ENV DEBIAN_FRONTEND noninteractive

EXPOSE 8888

RUN apt-get update && \
    apt-get --no-install-recommends install --yes \
    python3 python3-pip git \
    npm nodejs-legacy && \
    npm install -g configurable-http-proxy

RUN pip3 install --upgrade pip && \
    pip3 install setuptools && \
    pip3 install ipython
#    pip3 install ipython && \
#    pip3 install notebook

RUN pip3 install git+git://github.com/jupyterhub/jupyterhub && \
    pip3 install notebook
#    pip3 install git+git://github.com/jupyterhub/jupyterhub@267994b191fc72fbbaec00b1ad41627e6539fdae && \

COPY jupyterhub-singleuser /usr/local/bin/jupyterhub-singleuser

COPY singleuser.sh /srv/singleuser/singleuser.sh

RUN useradd -d /home/nugrid -m -c "" nugrid && \
    chown -R nugrid:nugrid /home/nugrid && \
    chmod 755 /usr/local/bin/jupyterhub-singleuser
#    chmod 755 /usr/local/bin/jupyterhub-singleuser && \
#    chmod 755 /srv/singleuser/singleuser.sh

USER nugrid

ENV HOME /home/nugrid

WORKDIR /home/nugrid

#test script
#RUN sh /srv/singleuser/singleuser.sh -h
CMD ["sh", "/srv/singleuser/singleuser.sh"]
