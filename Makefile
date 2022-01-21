.PHONY: dev run lint test build

dev:
	celery -A fikkie.main worker -B -l debug

run:
	celery -A fikkie.main worker -B -l info

lint:
	black --check .

unit:
	FIKKIE_CONFIG=/dev/null pytest --cov=fikkie --cov-report=xml --cov-fail-under=100

functional:
	bash ./tests/functional/test.sh

build:
	python -m build
