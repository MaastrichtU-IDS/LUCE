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
# -> Not needed for django_vm since jupyter itself was installed inside
# -> django_vm environment. So the ipykernel package is already available
# -> and the default Python 3 kernel uses django_vm environment.

# pip install ipykernel
# python -m ipykernel install --user --name=django_vm


# ==== PREPARE DJANGO ENVIRONMENT ====
# Prepare environment for Try Django tutorial

# Set up conda environment for try_django
# conda create -y --name try_django python

# Activate environment
# conda activate try_django

# Set up jupyter kernel inside virtual environment
# -> Here both is needed: the ipykernel package does not exist yet in the
# -> new environment. And installing the kernel in this environment allows
# -> to use this environment even if jupyter notebook server is called from
# -> another environment. E.g. jupyter notebbok running in django_vm but the
# -> kernel is acessing packages in try_django. In this case bash commands in
# -> jupyter will access a different python env than commands in python cells. 
# pip install ipykernel
# python -m ipykernel install --user --name=django_vm

# conda install -y django=2.2
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