#!/bin/bash
set -e

cd ~/catrius_blog_backend
git checkout master
git pull
poetry install --no-dev
python manage.py migrate
sudo service gunicorn restart
