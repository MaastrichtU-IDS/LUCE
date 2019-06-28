#!/usr/bin/env bash

sudo su - postgres
psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant'"
psql -c "CREATE DATABASE luce OWNER vagrant;"
sudo su - vagrant