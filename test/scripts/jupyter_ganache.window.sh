# Set window root path. Default is `$session_root`.
# Must be called before `new_window`.
window_root "~/"

# Create new window. If no argument is given, window name will be based on
# layout file name.
new_window "jupyter_ganache"
run_cmd "watch -t date"

# Split window into panes.
split_v 80
run_cmd "ls"