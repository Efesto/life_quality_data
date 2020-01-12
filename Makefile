install-service:
    cd service
	sudo cp humidity.service /etc/systemd/system
	sudo systemctl enable humidity.service

	sudo cp humidity-server.service /etc/systemd/system
	sudo systemctl enable humidity-server.service

install-deps:
    pip install -r requirements.txt

run:
	python3 humidity.py
