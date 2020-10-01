FROM ubuntu

MAINTAINER Pablo Ahumada "pablo.ahumada1@mail.udp.cl"
MAINTAINER Joaquín Fernández "joaquin.fernandez1@mail.udp.cl"

WORKDIR /irssi

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
&& apt-get install -y autoconf automake build-essential git libglib2.0-dev libncurses5-dev libssl-dev libtool lynx pkg-config

RUN git clone --branch 1.2.2 "https://github.com/irssi/irssi" && cd irssi/ \
&& ./autogen.sh \
&& make install

RUN useradd -m -r usuario

USER usuario

ENTRYPOINT ["irssi"]