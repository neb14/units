FROM 10.0.0.217:5000/base:latest


RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive && \
apt-get install -yq apache2 && \
a2enmod cgid && \
a2enconf serve-cgi-bin && \
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
rm -rf /tmp/*

ADD foo.cgi /usr/lib/cgi-bin/foo.cgi


EXPOSE 80:80

CMD [ "apache2ctl" , "-DFOREGROUND" ]
