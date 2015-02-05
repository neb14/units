FROM ubuntu:14.04

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive && \
apt-get dist-upgrade -y && \
apt-get install -y chef vim htop nethogs screen telnet wget curl lsof && \
apt-get install -y wget python python-pip python-dev libssl-dev libffi-dev bash nmap && \
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
