# Developer's guide

So you want to write a patch, fix a bug or implement a new feature? You're awesome,
thanks!


## Setting up a development environment

Start off by forking the fikkie GitHub repository and clone the fork.

```bash
git clone https://github.com/YOUR_USERNAME/fikkie
cd fikkie
```

Now create a virtual environment to prevent a dependency hell on your system.

```bash
python3 -m venv venv
source venv/bin/activate
```

Now that you're inside the virtual environment, install the dependencies:

```bash
pip install -r requirements.txt
pip install -r test-requirements.txt
```

Finally, fikkie will need a configuration file to send notifications. We could use
fikkie to setup it's working directory in ~/.fikkie.

```bash
pip install .
fikkie init
```

Now edit `~/.fikkie/config.yaml`:

```yaml
---
heartbeat:
  schedule:
    minute: '*'
    hour: '*'
```

This will make sure fikkie sends a heartbeat notification every minute.

The celery output will contain logs of the heartbeat notifications, but please check out
[Setting up a notifier](./notifiers) to configure a notifier.


## Useful commands

The project contains a Makefile to make your life a tiny bit easier. The most important
make commands are the following three:

```bash
make unit  # Run the unit tests
make lint  # Run the linter (black)
make dev   # Run fikkie with loglevel set to DEBUG
```
