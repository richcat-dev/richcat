# Colorize prompt
export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Set less command options
export LESS="-F -g -i -M -R -S -w -X -z-4"

alias install-richcat='_install_richcat'
function _install_richcat() {
    \pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ richcat==$@
}
