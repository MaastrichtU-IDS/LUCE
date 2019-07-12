# This script starts the jupyter and ganache server processes in the background

# Create detached tmux session from terminal
tmux new-session -d -s jupyter_ganache
tmux rename-window 'jupyter_ganache'

# Send in commands to start jupyter
tmux send-keys -t jupyter_ganache.0 'eval "$(conda shell.bash hook)"' ENTER
tmux send-keys -t jupyter_ganache.0 'conda activate luce_vm' ENTER
tmux send-keys -t jupyter_ganache.0 'jupyter notebook --no-browser --ip 0.0.0.0 --port=8889 --NotebookApp.token="luce" --notebook-dir=/vagrant/jupyter/' ENTER

# Select first window in session and split it
tmux select-window -t jupyter_ganache:0
tmux split-window -v

# Send in commands to start ganache
tmux send-keys -t jupyter_ganache.1 'eval "$(conda shell.bash hook)"' ENTER
tmux send-keys -t jupyter_ganache.1 'conda activate luce_vm' ENTER
tmux send-keys -t jupyter_ganache.1 'ganache-cli --mnemonic luce' ENTER


echo
printf "The Jupyter and Ganache servers are now running...\n\n"

printf "Jupyter is listening on an alternative port: 8889\n\n"

printf "Please visit http://127.0.0.1:8889 in the browser on your host machine.
The password for the jupyter environment is: luce\n"
echo

# echo "Open http://127.0.0.1:8888 to access the Django server"
# echo "The ganache blockchain running on LuceVM is available via http://127.0.0.1:8545"

# Attach session for quick debugging
#tmux attach-session -t jupyter_ganache

# The following resource helped me greatly in getting this approach to work:
# https://stackoverflow.com/questions/5447278/bash-scripts-with-tmux-to-launch-a-4-paned-window