FROM python:3.12-slim
RUN python3 -m pip install ansible
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    sshpass
WORKDIR /ansible