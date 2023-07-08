#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
sudo echo "Fake HTML content" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of directories to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/hbnb_static/d' /etc/nginx/sites-available/default
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
t#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
