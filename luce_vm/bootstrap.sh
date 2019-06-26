#!/usr/bin/env bash

# Bash commands to run after the VM has started

apt-get update

# ==== INSTALL APACHE ====

# Install apache web sever
apt-get install -y apache2
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi

cp /vagrant/prepare_system.sh /home/vagrant