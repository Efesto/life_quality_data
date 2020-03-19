from sensors import dht

try:
	humidity, temperature = dht.DHT().read()
	print("{}C {}%".format(temperature, humidity))
except KeyboardInterrupt:
	pass
