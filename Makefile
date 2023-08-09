install:
	pip install -r requirements.txt

stop:
	docker-compose down


build:
	docker-compose up --build
