#!/usr/bin/env bash

# ==== SETUP DATABASE ====
# Note: Need to use cat | bash for these commands to work

sudo su - postgres
psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant'"
psql -c "CREATE DATABASE luce OWNER vagrant;"
exit

# Make conda environment commands available in shell script
eval "$(conda shell.bash hook)"

# Ensure correct environment is activated
conda activate test_vm

# Perform DB migrations
python /vagrant/django/manage.py makemigrations
python /vagrant/django/manage.py migrate

# Create Django superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('vagrant', 'vagrant@luce.com', 'vagrant')" | python /vagrant/django/manage.py shell


# This file needs to be executed via cat