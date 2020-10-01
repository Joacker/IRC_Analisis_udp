FROM ubuntu
MAINTAINER Pablo Ahumada "pablo.ahumada1@mail.udp.cl"
MAINTAINER Joaquín Fernández "joaquin.fernandez1@mail.udp.cl"

WORKDIR /inspircd

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
&& apt-get install -y build-essential git

RUN git clone --branch v3.7.0 "https://github.com/inspircd/inspircd.git" \
&& cd inspircd/ \
&& ./configure --disable-interactive --gid 0 --uid 0 \
&& make install \
&& chown root -R ../inspircd/

COPY inspircd.conf /inspircd/inspircd/run/conf/inspircd.conf

RUN echo "cd /inspircd/inspircd && run/inspircd start --runasroot" >> ~/.bashrc

 

