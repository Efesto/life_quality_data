install-service:
	sudo cp service/life_quality_data-collector.service /etc/systemd/system
	sudo systemctl enable life_quality_data-collector.service

	# sudo cp service/life_quality_data-server.service /etc/systemd/system
	# sudo systemctl enable life_quality_data-server.service

remove-service:
	sudo rm /etc/systemd/system/life_quality_data-server.service
	sudo systemctl disable life_quality_data-server.service

	sudo rm /etc/systemd/system/life_quality_data-collector.service
	sudo systemctl disable life_quality_data-collector.service

install-deps:
	pip install -r requirements.txt

install-db:
	echo "deb https://repos.influxdata.com/ubuntu bionic stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
	sudo curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install influxdb -y
	sudo systemctl start influxd
	sudo systemctl enable influxd

	# TODO: init table
	# TODO: init db by storing creds
	# service influxdb start
	# influx
	# create database "readings"
	# CREATE USER admin WITH PASSWORD '' WITH ALL PRIVILEGES
	# CREATE USER collector WITH PASSWORD ''
	# GRANT ALL ON "readings" TO "collector"
	# CREATE USER dashboard WITH PASSWORD ''
	# GRANT READ ON "readings" TO "dashboard"
