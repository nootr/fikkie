dev:
	celery -A fikkie.main worker -B -l debug

run:
	celery -A fikkie.main worker -B -l info
