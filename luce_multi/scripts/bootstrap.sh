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

# Jupyter configuration file - define hashed password for notebook access
mkdir -p /home/vagrant/.jupyter && cp /vagrant/.config/jupyter_notebook_config.py $_
# Custom logo for Jupyter
mkdir -p /home/vagrant/.jupyter/custom && cp /vagrant/.config/custom.css $_
cp /vagrant/.config/logo.png /home/vagrant/.jupyter/custom
# Change folder permissions
sudo chown -R vagrant:vagrant /home/vagrant/.jupyter

# Copy scripts to vagrant home directory
cp /vagrant/scripts/* /home/vagrant