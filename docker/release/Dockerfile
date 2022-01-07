FROM revanthtiruveedhi/todobackend-base:latest
MAINTAINER Rev

COPY target /wheelhouse

RUN . /appenv/bin/activate && \
    pip3 install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse