#!/usr/bin/env bash

# ==== START DJANGO SERVER ====

# Make conda environment commands available in shell script
eval "$(conda shell.bash hook)"

# Activate correct environment
conda activate test_vm

# Run server
python /vagrant/django/manage.py runserver 0.0.0.0:8000

# This can be included in run_.. server scripts as well as tmux script (run this server in new pane/window in tmux)