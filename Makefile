DOCKER_REGISTRY ?= lunch.voter.io
IMAGE_NAME ?= lunch-voter
TAG ?= $(shell git rev-parse --short HEAD)
LOCAL_DB_NAME ?= lunch_voter

.DEFAULT_GOAL := dev

.PHONY: dev test cover

test:
	pytest

cover:
	go test -cover ./...  -coverprofile=coverage.out && go tool cover -html=coverage.out

dev:
	fastapi dev src/main.py

migrate-up:
	migrate -source file://migrations/ \
	-database "postgres://postgres:12345@localhost:5432/$(LOCAL_DB_NAME)?sslmode=disable" up

migrate-down:
	migrate -source file://migrations/ \
	-database "postgres://postgres:12345@localhost:5432/$(LOCAL_DB_NAME)?sslmode=disable" down

docker-build:
	docker build --no-cache -t=$(IMAGE_NAME):latest .

docker-push:
	docker push $(DOCKER_REGISTRY)/$(IMAGE_NAME):$(TAG)

docker-push-latest:
	docker tag $(DOCKER_REGISTRY)/$(IMAGE_NAME):$(TAG) $(DOCKER_REGISTRY)/$(IMAGE_NAME):latest
	docker push $(DOCKER_REGISTRY)/$(IMAGE_NAME):latest