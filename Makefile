install-service:
	sudo cp service/life_quality_data-collector.service /etc/systemd/system
	sudo systemctl enable life_quality_data-collector.service

remove-service:
	sudo rm /etc/systemd/system/life_quality_data-server.service
	sudo systemctl disable life_quality_data-server.service

install-deps:
	pip install -r requirements.txt

install-db:
	echo "deb https://repos.influxdata.com/ubuntu bionic stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
	curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
		
	sudo apt-get install influxdb -y
	influx -import -path=db.import -precision=s

install-nginx:
	sudo apt-get install nginx -y
	cp nginx/grafana_viewer /etc/nginx/sites-enabled/default
	sudo systemctl restart nginx.service

install-grafana:
	sudo apt-get install apt-transport-https software-properties-common -y
	wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install grafana
	sudo systemctl enable grafana-server.service
	sudo systemctl start grafana-server
	sudo systemctl status grafana-server