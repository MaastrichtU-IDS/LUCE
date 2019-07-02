#!/usr/bin/env bash

# Bash commands to run after the VM has started

# Install GNU compiler utitilities 
# (required for web3 installation) 

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
conda create -y --name luce_vm python

# Activate environment
conda activate luce_vm

# ==== INSTALL JUPYTER & KERNEL ====

# Install Jupyter
conda install -y jupyter

# Set up jupyter kernel for luce python environment
# pip install ipykernel
python -m ipykernel install --user --name=luce_vm

# ==== INSTALL WEB3 ====

pip install web3
pip install py-solc-x

# ==== INSTALL SOLIDITY COMPILER ====

# We use the py-colc-x package from the command line to install the solidity compiler
# v0.4.25 is the latest stable v4 version available on github
python -m solcx.install v0.4.25


# ==== INSTALL NODE.JS AND GANACHE ====

# 1) Install Node Version Manager
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
export NVM_DIR="/home/vagrant/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# 2) Install node.js
nvm install node 

# 3) Install Ganache
npm install -g ganache-cli

# ==== COMPLETION MESSAGE ====

echo
echo "Thank you for your patience =)"
echo "The LuceVM environment is ready now"
echo
echo "Please run the following command to start the servers:"
echo "$ bash run_servers_tmux.sh"

# echo "Please run the following command to finalise the setup:"
# echo "$ source ~/.bashrc"
# exec bash

# echo
# echo "Open http://127.0.0.1:4567 in your browser for further instructions on how to continue."