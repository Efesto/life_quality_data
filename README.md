The idea of this project to offer a minimal yet effective and robust way to setup your own quality of life data collector using a series of sensors and a Raspberry PI.
Currently it collects data related to Humidity, Temperature and CO2 density.
This repo DOES NOT explain how to configure the individual sensor, for such refer to the various guides on the net.

## Components:
### Software:
- InfluxDB for data collection
- Grafana for data visualization
- Pyhton3
- Nginx (for dashboard view-only configuration without authentication)

### Hardware:
- CCS811 Sensor
- DHT22 Sensor

## Installation

1. `bash -c "$(wget -O- https://raw.githubusercontent.com/Efesto/life_quality_data/master/install-full.sh)"` Full version
2. `bash -c "$(wget -O- https://raw.githubusercontent.com/Efesto/life_quality_data/master/install-collector.sh)"` Collector only
3. Configure .env file content by copying .env.sample file
4. Configure CCS811 (see following)
   
## How to configure the CCS811
1. We need to enable the I2C bus so we can communicate with the sensor with `sudo raspi-config`
2. add `dtparam=i2c_baudrate=10000` to `/boot/config.txt`
3. check with `sudo i2cdetect -y 1`

## How to configure Grafana for authentication-free dashboard
1. refer to https://grafana.com/docs/grafana/latest/installation/configuration/ for adding the following to grafana config
```
[auth.proxy]
auto_sign_up = true
enabled = true
```
