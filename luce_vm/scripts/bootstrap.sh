#!/usr/bin/env bash

# Bash commands to run during VM initialization
# Customise motd
rm /etc/update-motd.d/*
cp /vagrant/.config/luce_motd /etc/update-motd.d/00-header

# ==== INSTALL APACHE ====

# Install apache web sever
apt-get install -y apache2
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi

# Copy jupyter configuration into VM & make vagrant owner of folder
mkdir -p /home/vagrant/.jupyter && cp /vagrant/.config/jupyter_notebook_config.py $_
mkdir -p /home/vagrant/.jupyter/custom && cp /vagrant/.config/custom.css $_
sudo chown -R vagrant:vagrant /home/vagrant/.jupyter

# Copy scripts to vagrant home directory
cp /vagrant/scripts/* /home/vagrant