#!/usr/bin/bash

set -e

# Create virtualenv
python3 -m venv venv
source venv/bin/activate

# Install fikkie
pip install .

# Configure fikkie
fikkie init

ls ~/.fikkie
grep "^## SSH config$" ~/.fikkie/config.yaml

cat > ~/.fikkie/config.yaml << EOF
---
ssh:
  username: foo

servers:
  localhost:
    - description: 'SSH Daemon'
      command: 'echo foo'
      expected: 'foo'
EOF

# Run fikkie
fikkie start

sleep 1

ls ~/.fikkie/fikkie.log
ps -p $(cat ~/.fikkie/fikkie.pid) | grep fikkie

# Get fikkie status
fikkie status | grep "^Daemon running: true$"
fikkie status | grep "description: SSH Daemon"

# Stop fikkie
fikkie stop

sleep 5

[ ! -f ~/.fikkie/fikkie.pid ]
fikkie status | grep "^Daemon running: false$"

# Cleanup
rm -rf ~/.fikkie
rm -rf venv
