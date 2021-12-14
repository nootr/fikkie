from celery import Celery

import os

from .config import BROKER_DIR
from .watchdog import WatchDog


app = Celery(__name__)
app.conf.update(
    {
        "broker_url": "filesystem://",
        "broker_transport_options": {
            "data_folder_in": os.path.join(BROKER_DIR, "out"),
            "data_folder_out": os.path.join(BROKER_DIR, "out"),
            "data_folder_processed": os.path.join(BROKER_DIR, "processed"),
        },
        "result_persistent": False,
        "task_serializer": "json",
        "result_serializer": "json",
        "accept_content": ["json"],
    }
)
app.conf.beat_schedule = {
    'tick': {
        'task': 'fikkie.main.tick',
        'schedule': 60
    },
}


@app.task
def tick():
    watchdog = WatchDog()
    watchdog.tick()
