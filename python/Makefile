minikube:
	minikube start --vm-driver=none

build:
	cd user && docker build -t yafig-user-api-server .

run:
	docker run -it --rm -p 5000:5000 -v $(shell pwd)/user:/app yafig-user-api-server bash

run-db:
	docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password --name yafig-mysql mysql:5.6

db:
	mysql -uroot -ppassword --port 3306 -h 127.0.0.1 yafig
