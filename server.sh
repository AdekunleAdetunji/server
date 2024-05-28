#!/bin/bash

# activate the server daemon virtual environment
source env/bin/activate

# start the daemon
exec python server_script.py
