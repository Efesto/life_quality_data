from sensors import dht, ccs811

try:
	humidity, temperature = dht.DHT().read()
	eCO2, TVOC, temp = ccs811.CCS811().read()
	print("DHT22 {}C {}%".format(temperature, humidity))
	print("CCS811 {} eCO2 {} TVOC {}C".format(eCO2, TVOC, temp))
except KeyboardInterrupt:
	pass
