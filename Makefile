install-service:
	sudo cp humidity.service /etc/systemd/system
	sudo systemctl enable humidity.service
run:
	python3 humidity.py
