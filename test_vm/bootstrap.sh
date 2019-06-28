#!/usr/bin/env bash

# Bash commands to run during VM initialization

# ==== INSTALL & CONFIGURE TMUXIFIER ====
# Tmuxifier allows me to start a tmux configuration from a script
# This way we can run the jupyter and ganache servers conveniently 
# in a tmux background process.

# Install Tmux
git clone https://github.com/jimeh/tmuxifier.git ~/.tmuxifier
export PATH="$HOME/.tmuxifier/bin:$PATH"
echo 'eval "$(tmuxifier init -)"' >> ~/.bashrc