#!/bin/bash


# Update system
sudo apt update -y && sudo apt upgrade -y sudo apt

# Function to check if a package is installed
package_installed() {
    dpkg-query -W -f='${Status}' "$1" 2>/dev/null | grep -c "ok installed"
}

# Check if python3-venv package is installed, if not, install it
if ! package_installed python3-venv; then
    echo "python3-venv package is not installed. Installing..."
    sudo apt install -y python3.8-venv
fi

# Create a new virtual environment called 'env' if it doesn't exist
if [ ! -d "$(pwd)/env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $(pwd)/env
fi

# activate virtual environment for requirement.txt installation
source env/bin/activate

echo "Installing dependencies from requirements.txt..."
pip install -r $(pwd)/requirements.txt


# Define the file path for the service file
service_file_path="/etc/systemd/system/server.service"

# Create the service file content using a here-document
cat <<EOF | sudo tee $service_file_path > /dev/null
[Unit]
Description=Python Server Service
After=network.target

[Service]
Type=simple
ExecStart=$(pwd)/server.sh
Restart=on-failure
WorkingDirectory=$(pwd)
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

# Reload the systemd daemon to apply the new service file
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable server.service

# Start the service
sudo systemctl start server.service

# Check the status of the service
sudo systemctl status server.service
