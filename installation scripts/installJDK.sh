#!/bin/bash

# Define the JDK version and download URL
JDK_VERSION="21"
JDK_TAR="jdk-${JDK_VERSION}_linux-x64_bin.tar.gz"
JDK_URL="https://download.oracle.com/java/${JDK_VERSION}/latest/${JDK_TAR}"
INSTALL_DIR="/usr/local/java"

# Function to install the JDK
install_jdk() {
    echo "Downloading JDK from ${JDK_URL}..."
    wget -q "${JDK_URL}" -O "${JDK_TAR}"

    echo "Extracting JDK..."
    sudo mkdir -p "${INSTALL_DIR}"
    sudo tar -xzf "${JDK_TAR}" -C "${INSTALL_DIR}"

    # Get the extracted directory name
    JDK_DIR=$(ls -d ${INSTALL_DIR}/jdk-*)

    echo "Setting up environment variables..."
    echo "export JAVA_HOME=${JDK_DIR}" | sudo tee /etc/profile.d/jdk.sh
    echo 'export PATH=$JAVA_HOME/bin:$PATH' | sudo tee -a /etc/profile.d/jdk.sh

    # Clean up
    rm "${JDK_TAR}"

    echo "JDK installed successfully. Sourcing environment variables..."
    
    # Source the profile.d script to apply changes
    source /etc/profile.d/jdk.sh
}

# Check for wget
if ! command -v wget &> /dev/null; then
    echo "wget not found, installing wget..."
    sudo apt-get update
    sudo apt-get install -y wget
fi

# Run the installation function
install_jdk

# Inform the user to reload their environment
echo "To apply the changes in new terminal sessions, please run: source /etc/profile.d/jdk.sh"
