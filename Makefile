install-service:
	sudo cp service/life_quality_data-collector.service /etc/systemd/system
	sudo systemctl enable life_quality_data-collector.service

remove-service:
	sudo rm /etc/systemd/system/life_quality_data-server.service
	sudo systemctl disable life_quality_data-server.service

install-deps:
	pip3 install -r requirements.txt

install-db:
	echo "deb https://repos.influxdata.com/ubuntu bionic stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
	curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
		
	sudo apt-get install influxdb -y
	influx -import -path=db.import -precision=s

install-nginx:
	sudo apt-get install nginx -y
	sudo cp nginx/grafana_viewer /etc/nginx/sites-enabled/default
	sudo systemctl restart nginx.service

install-grafana:
	sudo apt-get install -y adduser libfontconfig1
	wget https://dl.grafana.com/oss/release/grafana_7.0.3_armhf.deb
	sudo dpkg -i grafana_7.0.3_armhf.deb
	sudo systemctl enable grafana-server.service
	sudo systemctl start grafana-server
	sudo systemctl status grafana-server
