#!/usr/bin/env bash
# Set proper permissions
sudo chown ubuntu:www-data /var/log/uwsgi
sudo chmod 775 /var/log/uwsgi

# Reload systemd
sudo systemctl daemon-reload
sudo systemctl restart uwsgi
sudo systemctl status uwsgi
