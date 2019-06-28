#!/usr/bin/env bash

# Make conda environment commands available in shell script
eval "$(conda shell.bash hook)"

# Ensure correct environment is activated
conda activate luce_vm

# Run Ganache server
ganache-cli --mnemonic luce
