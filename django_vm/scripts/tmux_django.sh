# This script starts the django server process in the background

# Create detached tmux session from terminal
tmux new-session -d -s django # -d flag for 'detached'
tmux rename-window 'django'

# Send in commands to start django
tmux send-keys -t django.0 'eval "$(conda shell.bash hook)"' ENTER
tmux send-keys -t django.0 'conda activate try_django' ENTER
tmux send-keys -t django.0 'python /vagrant/try_django/manage.py runserver 0.0.0.0:8000' ENTER

# Attach session for quick debugging
#tmux attach-session -t django