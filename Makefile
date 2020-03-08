install-service:
	sudo cp service/life_quality_data-collector.service /etc/systemd/system
	sudo systemctl enable life_quality_data-collector.service

	sudo cp service/life_quality_data-server.service /etc/systemd/system
	sudo systemctl enable life_quality_data-server.service

remove-service:
	sudo rm /etc/systemd/system/life_quality_data-server.service
	sudo systemctl disable life_quality_data-server.service

	sudo rm /etc/systemd/system/life_quality_data-collector.service
	sudo systemctl disable life_quality_data-collector.service

install-deps:
	pip install -r requirements.txt

db-create_table:
	python3 repository/create_table.py
