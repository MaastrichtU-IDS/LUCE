#!/usr/bin/env bash

# ==== INSTALL DJANGO ====

# Activate correct environment
conda activate test_vm

# Install django and postgres package for python
pip install django psycopg2

# This can be included in general installation in prepare_system.sh