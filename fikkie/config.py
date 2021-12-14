import logging
import os
import yaml


__all__ = ['BASE_DIR', 'CONFIG_FILE', 'BROKER_DIR', 'CONFIG']

BASE_DIR = os.getenv('FIKKIE_BASE_DIR', os.path.expanduser('~/.fikkie'))
CONFIG_FILE = os.getenv('FIKKIE_CONFIG', os.path.join(BASE_DIR, 'config.yaml'))
BROKER_DIR = os.getenv('FIKKIE_BROKER_DIR', os.path.join(BASE_DIR, 'broker'))

needed_dirs = [
    BASE_DIR,
    BROKER_DIR,
    os.path.join(BROKER_DIR, 'out'),
    os.path.join(BROKER_DIR, 'processed')
]
for directory in needed_dirs:
    if not os.path.isdir(directory):
        os.mkdir(directory)
        logging.info(f"Created directory: {directory}")


def load_config(filename):
    try:
        with open(filename, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        logging.error(f"Could not find config file: {e}")
        exit(1)
    except yaml.YAMLError as e:
        logging.error(f"Could not parse config: {e}")
        exit(1)


CONFIG = load_config(CONFIG_FILE)
