.PHONY: dev run lint test build publish

dev:
	celery -A fikkie.main worker -B -l debug

run:
	celery -A fikkie.main worker -B -l info

lint:
	black --check

test:
	FIKKIE_CONFIG=/dev/null pytest

build:
	python -m build
