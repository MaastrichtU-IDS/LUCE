#!/usr/bin/env bash

# ==== SETUP DATABASE ====
# Note: Need to use cat | bash for these commands to work

sudo su - postgres
psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant'"
psql -c "CREATE DATABASE luce OWNER vagrant;"
exit

# This file needs to be executed via cat
# Easiest to combine remaining files with this one so all are in one step