
# IRC_Analysis_TRS_UDP
Dockerfiles para montar un cliente y servidor IRC de manera muy facil, con el fin de generar y analizar el trafico IRC generado por los mismos.
Por Pablo Ahumada y Joaquín Fernández 

## Instalación

Clona el directorio:
```sh
$ git clone https://github.com/ElSacoWeant/IRC_Analysis_TRS_UDP
```

Para instalar el servidor Inspircd:
```sh
$ docker build -t inspircd IRC_Analysis_TRS_UDP/Servidor/
```

Para instalar el cliente Irssi:
```sh
$ docker build -t irssi IRC_Analysis_TRS_UDP/Cliente/
```


## Uso
Crear un contenedor con la imagen del servidor:
```sh
$ docker run -it -p 6667:6667 --name servidorIRC inspircd
```

Crear un contenedor con la imagen del cliente:
```sh
$ docker run -it --name clienteIRC irssi
```


## Video capturando trafico generado entre el servidor y cliente

[![Watch the video](https://img.youtube.com/vi/LIOw5wZKxmw/hqdefault.jpg)](https://youtu.be/LIOw5wZKxmw)

