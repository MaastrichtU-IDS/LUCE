#!/usr/bin/env bash

# Bash commands to run during VM initialization

# Customise motd
rm /etc/update-motd.d/*
cp /vagrant/.etc/luce_motd /etc/update-motd.d/00-header

# Copy scripts to vagrant user directory
cp /vagrant/scripts/* /home/vagrant
