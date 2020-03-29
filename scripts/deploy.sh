#!/bin/bash
set -e

cd ~/catrius_blog_backend
git pull
poetry install --no-dev
python manage.py migrate
sudo service gunicorn restart
