#!/bin/bash

# Update all system packages to latest versions
sudo dnf update -y

# Install git
sudo dnf install git -y

# Install Java 21 (Jenkins requires Java 17 or 21)
sudo dnf install java-21-amazon-corretto -y

# Download Jenkins repository file
sudo wget -O /etc/yum.repos.d/jenkins.repo \
https://pkg.jenkins.io/redhat-stable/jenkins.repo

# Import Jenkins GPG key to verify Jenkins packages
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

# Install Jenkins from the official repository
sudo dnf install jenkins -y

# Start Jenkins
sudo systemctl start jenkins

# Enable Jenkins to start automatically on system reboot
sudo systemctl enable jenkins

# Display Jenkins initial admin password (used for first-time login)
echo "Jenkins Initial Admin Password:"
sudo cat /var/lib/jenkins/secrets/initialAdminPassword