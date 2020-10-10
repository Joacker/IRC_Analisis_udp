FROM ubuntu:20.04

MAINTAINER Pablo Ahumada "pablo.ahumada1@mail.udp.cl"
MAINTAINER Joaquín Fernández "joaquin.fernandez1@mail.udp.cl"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y\
&& apt-get upgrade -y\
&& apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git net-tools iptables vim -y\

RUN pip3 install git+https://github.com/kti/python-netfilterqueue\
&& pip3 install polymorph

ENTRYPOINT [ "polymorph" ]
