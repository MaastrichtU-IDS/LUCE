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
# This command allows the current shell (also in script) to access conda commands
eval "$(/home/vagrant/miniconda/bin/conda shell.bash hook)" 
conda init
source /home/vagrant/.bashrc

# 4) Clean up 
rm /home/vagrant/miniconda.sh

# ==== CONDA ENVIRONMENT ====

# Set up new conda environment
conda create -y --name django_vm python

# Activate environment
conda activate django_vm

# ==== INSTALL JUPYTER & KERNEL ====

# Install Jupyter
conda install -y jupyter

# Set up jupyter kernel inside virtual environment
# pip install ipykernel
python -m ipykernel install --user --name=django_vm


# ==== INSTALL DJANGO ====

# conda install django=2.2
# pip install sqlparse


# ==== COMPLETION MESSAGE ====

echo
echo "Everything is ready :D"
echo

echo "Please run the following command to finalise the setup:"
echo "(Not sure if needed, try without and only do if needed.)"
echo "$ source ./bashrc"
echo
exec bash