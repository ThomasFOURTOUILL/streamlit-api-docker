.PHONY: del-images

install: 
	pip install -r requirements.txt

clean:
	docker rmi -f $$(docker images -a -q)

up:
	docker-compose up --build

build: clean up

curl:
	curl -X 'GET'   'http://localhost:8000/items/1?q=test' -H 'accept: ap2lication/json'
	echo " "

empty:
	docker build -t empty -f Dockerfile.noobject .
	docker run -it --name mon_conteneur empty