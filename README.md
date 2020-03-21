__How to configure the CCS811__
1. We need to enable the I2C bus so we can communicate with the sensor with `sudo raspi-config`
2. add `dtparam=i2c_baudrate=10000` to `/boot/config.txt`
3. check with `sudo i2cdetect -y 1`