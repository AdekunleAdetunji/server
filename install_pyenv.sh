#!/bin/bash

# Update package list and install dependencies
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
     libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
     libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
     liblzma-dev python-openssl git

# Clone pyenv repository
if [ ! -d "$HOME/.pyenv" ]; then
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
else
    echo "pyenv is already installed."
fi

# Add pyenv to bash so that it loads every time you open a terminal
if ! grep -q 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bashrc; then
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
fi

# Apply changes to the current session
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# restart shell for changes to take effect
exec "$SHELL"

# Ensure pyenv is updated
if command -v pyenv >/dev/null; then
    echo "pyenv successfully installed"
    pyenv update
else
    echo "pyenv installation failed"
    exit 1
fi

# Install Python 3.10.0
pyenv install 3.10.0

# Set Python 3.10.0 as the global default version
pyenv global 3.10.0

# Verify the installation
if pyenv versions | grep -q "3.10.0"; then
    echo "Python 3.10.0 installed successfully."
else
    echo "Python 3.10.0 installation failed."
    exit 1
fi

# Check the Python version
python --version
