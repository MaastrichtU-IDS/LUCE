# This script starts the jupyter server process in the background

# Create detached tmux session from terminal
tmux new-session -d -s jupyter # -d flag for 'detached'
tmux rename-window 'jupyter'

# Send in commands to start jupyter
tmux send-keys -t jupyter.0 'eval "$(conda shell.bash hook)"' ENTER
tmux send-keys -t jupyter.0 'conda activate django_vm' ENTER
tmux send-keys -t jupyter.0 'jupyter notebook --no-browser --ip 0.0.0.0 --NotebookApp.token="django" --notebook-dir=/vagrant/jupyter/' ENTER

# Attach session for quick debugging
#tmux attach-session -t jupyter