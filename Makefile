.PHONY: del-images

install: 
	pip install -r requirements.txt

del-images:
	docker rmi -f $$(docker images -a -q)

up:
	docker-compose up --build

build: del-images up

curl:
	curl -X 'GET'   'http://localhost:8000/items/1?q=test' -H 'accept: ap2lication/json'
	echo " "