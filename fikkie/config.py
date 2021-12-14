import logging
import os
import yaml


__all__ = ['BASE_DIR', 'CONFIG_FILE', 'BROKER_DIR', 'CONFIG']

BASE_DIR = os.getenv('FIKKIE_BASE_DIR', os.path.expanduser('~/.fikkie'))
CONFIG_FILE = os.getenv('FIKKIE_CONFIG', os.path.join(BASE_DIR, 'config.yaml'))
BROKER_DIR = os.getenv('FIKKIE_BROKER_DIR', os.path.join(BASE_DIR, 'broker'))

CONFIG_TEMPLATE = """---
## SSH config
# Fikkie needs to know which user to use to login into the servers. This will
# default to "fikkie".
#
# Example:
#
# ssh:
#   username: fikkie

## Servers
# This is where you specify the commands fikkie needs to execute over SSH to
# test them.
#
# Example:
#
# servers:
#   jhartog.dev:
#     - description: "HTTP code jhartog.dev"
#       command: 'curl -s -o /dev/null -w "%{http_code}" jhartog.dev'
#       expected: '200'
#     - description: "MariaDB"
#       command: 'sudo systemctl status mariadb | grep "Active: active" -c'
#       expected: '1'

## Notifiers
# If you want fikkie to notify state changes/problems, you'll need to specify
# the notifiers here.
#
# Example:
#
# notifiers:
#   - type: telegram
#     token: 'foo'
#     chat_id: 1234567
"""

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


def create_config_template(filename) -> None:
    """Create a config template at the given location."""
    try:
        with open(filename, 'x') as f:
            f.write(CONFIG_TEMPLATE)
    except Exception as e:
        logging.error(f"Could not write config template at {filename}: {e}")
        exit(1)


def load_config(filename: str) -> dict:
    try:
        with open(filename, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        create_config_template(filename)
        logging.warning(f"Created a config template at {filename}.")
        exit(0)
    except yaml.YAMLError as e:
        logging.error(f"Could not parse config: {e}")
        exit(1)


CONFIG = load_config(CONFIG_FILE)
