# Installation

Installing fikkie is easy!

```bash
pip install fikkie
fikkie init
```

Fikkie works with Python 3.8 or higher.


## Running fikkie in a Docker container

There is a Docker image for fikkie available, so just run it while binding your
configuration file and you're ready.

```bash
docker run \
  --mount type=bind,source=${PWD}/config.yaml,target=/root/.fikkie/config.yaml \
  nootr/fikkie:latest
```

This snippet assumes `config.yaml` lives in your current directory. If it does not,
please change the value of `source=`.
