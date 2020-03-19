from repository import dht

try:
	print("{}C {}%".format(dht.DHT().read()))
except KeyboardInterrupt:
	pass
