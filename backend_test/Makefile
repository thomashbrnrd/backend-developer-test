CONTAINER_NAME = sorted_api

local:
	# start develop environment
	docker compose up

build:
	# start develop environment
	docker compose build

bash:
	docker exec -it $(CONTAINER_NAME) bash

test:
	docker exec -it $(CONTAINER_NAME) bash -c "pytest -v"

lint:
	black -v */*.py

lint-check:
	black -v --check */*.py
