# This script starts jupyter and ganache server processes in the background

# Create tmux session from terminal without entering it and execute command
tmux new-session -d -s jupyter_ganache 'exec watch -t date'
tmux rename-window 'jupyter_ganache'

# Select first window in session and split it
tmux select-window -t jupyter_ganache:0
tmux split-window -v 'exec watch -t date'
# tmux split-window -v -t 0 'exec pfoo "rake ts:start"'
# tmux split-window -v -t 1 'exec pfoo'
# tmux -2 attach-session -t foo