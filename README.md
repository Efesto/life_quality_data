__How to configure the CCS811__
1. We need to enable the I2C bus so we can communicate with the sensor with `sudo raspi-config`
2. add `dtparam=i2c_baudrate=10000` to `/boot/config.txt`
3. check with `sudo i2cdetect -y 1`


__How to configure Grafana with public viewable dashboards__
1. Install Grafana
2. set it as service
3. refer to https://grafana.com/docs/grafana/latest/installation/configuration/ for adding the following to grafana config
```
[auth.proxy]
auto_sign_up = true
enabled = true
```
4. Install nginx
   1. `sudo apt-get install nginx`
   2. `cp nginx/grafana_viewer /etc/nginx/sites-enabled/default`
   3. `sudo systemctl restart nginx.service`