#!/bin/bash

if pyenv versions | grep -q "3.10.12"; then
    echo "Python 3.10.12 already installed"
    exit 0
fi

# Install Python 3.10.12
pyenv install 3.10.12

# Set Python 3.10.12 as the global default version
pyenv global 3.10.12

# Verify the installation
if pyenv versions | grep -q "3.10.12"; then
    echo "Python 3.10.12 already installed"
else
    echo "Python 3.10.12 installation failed."
fi

# Check the Python version
python --version
