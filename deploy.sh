#!/bin/bash
PROJECT_DIR="CI-CDRepro"
cd  "$PROJECT_DIR"
# clone the new commit sto that directory 
git pull origin main
cd 

sudo cp CI-CDRepro/* /var/www/html

sudo systemctl restart nginx

echo "Deployment complete."