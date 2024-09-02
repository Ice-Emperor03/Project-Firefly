#!/bin/bash

# Update the package list
echo "Updating package list..."
sudo apt update

# Install default JDK
echo "Installing default JDK..."
sudo apt install -y default-jdk

# Confirm installation
echo "JDK installation completed. Verifying installation..."
java -version
javac -version
