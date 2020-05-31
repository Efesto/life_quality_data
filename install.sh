#!/bin/bash

set -e

# packages
apt-get install git python3 wget -y

# pull repository
git clone https://github.com/Efesto/life_quality_data.git ~/life_quality_data
cd ~/life_quality_data

# install influx db
make install-db

# configure service
make install-service

# install Grafana
make install-grafana

# configure nginx
make install-nginx

