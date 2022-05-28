FROM ubuntu:18.04
RUN apt-get update && \
      apt-get -y install sudo
RUN useradd -u 8877 docker && echo "docker:docker" | chpasswd && adduser docker sudo
RUN chmod -R 777 /home
USER docker
CMD /bin/bash