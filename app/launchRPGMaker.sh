#!/bin/sh

sudo apt-get update
sudo apt-get install -y python3 python3-pip
sudo pip3 install flask flask_wtf flask_bootstrap
python3 /usr/local/app/RPGMaker.py &
