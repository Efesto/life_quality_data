#!/bin/bash

# packages
sudo apt-get install git python3 python3-pip wget -y

# pull repository
git clone https://github.com/Efesto/life_quality_data.git ~/life_quality_data
cd ~/life_quality_data

# install deps
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
make install-deps

# install influx db
make install-db

# configure service
make install-service

# install Grafana
make install-grafana

# configure nginx
make install-nginx

