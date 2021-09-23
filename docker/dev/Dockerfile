FROM jmenga/todobackend-base:latest
MAINTAINER Rev

RUN apt-get update && \
    apt-get install -qy python-dev libmysqlclient-dev

RUN . /appenv/bin/activate && \
    apt install python3-pip -y && \
    pip3 install wheel --upgrade

ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

VOLUME /wheelhouse

VOLUME /build

VOLUME /reports

COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

ENTRYPOINT ["test.sh"]
CMD ["python3", "manage.py", "test", "--noinput"]

COPY src /application
WORKDIR /application