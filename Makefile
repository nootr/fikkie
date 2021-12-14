run:
	celery -A fikkie.main worker -B -l info
