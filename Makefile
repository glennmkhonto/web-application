install:
	pip install -r requirements.txt

down:
	docker-compose down


up:
	docker-compose up --build
