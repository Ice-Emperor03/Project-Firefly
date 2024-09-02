#!/bin/bash

# Update the package list
sudo apt-get update

# Install apksigner
sudo apt-get install -y apksigner

# Verify installation
if command -v apksigner &> /dev/null; then
    echo "apksigner has been successfully installed."
else
    echo "Failed to install apksigner."
    exit 1
fi
