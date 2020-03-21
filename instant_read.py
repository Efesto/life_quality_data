from sensors import dht, ccs811

try:
	humidity, temperature = dht.DHT().read()
	eCO2, TVOC = ccs811.CCS811().read()
	print("DHT22 {}C {}%".format(temperature, humidity))
	print("CCS811 CO2 {} PPM, TVOC {}PPB".format(eCO2, TVOC))
except KeyboardInterrupt:
	pass
