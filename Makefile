install:
	pip install -r requirements.txt

down:
	docker-compose -f docker-compose.yml down


up:
	docker-compose -f docker-compose.yml up --build -d
