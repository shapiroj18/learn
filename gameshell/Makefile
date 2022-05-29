.PHONY: build, run

current_dir = $(shell pwd)

build:
	docker build -t gameshell .

run: build
	docker run -it -v $(current_dir)/home:/home gameshell