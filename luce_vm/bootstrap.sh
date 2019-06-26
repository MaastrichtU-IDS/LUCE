#!/usr/bin/env bash

apt-get update

# Set up apache web sever
apt-get install -y apache2
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi