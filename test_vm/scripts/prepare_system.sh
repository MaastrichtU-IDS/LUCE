#!/usr/bin/env bash

# Bash commands to run after the VM has started

# Install GNU compiler utitilities 
# (required for web3 installation and also for psycopg2 (PostgreSQL)) 

sudo apt --assume-yes install build-essential

# ==== INSTALL ANACONDA ====

# 1) Download installer script
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/vagrant/miniconda.sh

# 2) Install miniconda
bash /home/vagrant/miniconda.sh -b -p /home/vagrant/miniconda

# 3) Add to path and initialize
eval "$(/home/vagrant/miniconda/bin/conda shell.bash hook)"
conda init
source /home/vagrant/.bashrc

# 4) Clean up 
rm /home/vagrant/miniconda.sh

# ==== CONDA ENVIRONMENT ====

# Set up new conda environment
conda create -y --name test_vm python

# Activate environment
conda activate test_vm

# ==== INSTALL POSTGRESQL ====

sudo apt-get --assume-yes install postgresql postgresql-contrib libpq-dev 


# ==== INSTALL DJANGO ====

# Install django and postgres package for python
pip install django psycopg2


# ==== COMPLETION MESSAGE ====

echo
echo "Everything is ready."
echo

echo "Please run the following command to finalise the setup:"
echo "$ cat setup_database.sh | bash"
echo
exec bash