install-service:
	sudo cp service/humidity-collector.service /etc/systemd/system
	sudo systemctl enable humidity-collector.service

	sudo cp service/humidity-server.service /etc/systemd/system
	sudo systemctl enable humidity-server.service

remove-service:
	sudo rm /etc/systemd/system/humidity-server.service
	sudo systemctl disable humidity-server.service

	sudo rm /etc/systemd/system/humidity-collector.service
	sudo systemctl disable humidity-collector.service

install-deps:
	pip install -r requirements.txt

run:
	python3 humidity.py
