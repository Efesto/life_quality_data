install-service:
	sudo cp humidity.service /etc/systemd/system
	sudo systemctl enable humidity.service

	sudo cp humidity-server.service /etc/systemd/system
	sudo systemctl enable humidity-server.service

install-deps:
	pip install Adafruit_Python_DHT

run:
	python3 humidity.py
