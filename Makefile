.PHONY: dev run lint test build publish

dev:
	celery -A fikkie.main worker -B -l debug

run:
	celery -A fikkie.main worker -B -l info

lint:
	black --check

unit:
	FIKKIE_CONFIG=/dev/null pytest

functional:
	./tests/functional/test.sh

build:
	python -m build
