# Colorize prompt
export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Set less command options
export LESS="-F -g -i -M -R -S -w -X -z-4"

# Alias for act command
alias act="~/bin/act"