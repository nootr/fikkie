#!/usr/bin/bash

# This wrapper will daemonize the celery worker if the "-d" parameter is set.

USAGE="fikkie [-d|--daemonize] [-h|--help]

  Usage:
      fikkie
          Run fikkie.
      fikkie -d
          Start a fikkie daemon.
      fikkie -h
          Show this text.

Check out the docs or README at github.com/nootr/fikkie for more info."

DAEMONIZE=0

case "$1" in
  -d|--daemonize) DAEMONIZE=1;;
  -h|--help)      echo "$USAGE"; exit 0;;
esac

if [ "$DAEMONIZE" -eq "1" ]; then
  # Double fork to daemonize
  (celery -A fikkie.main worker -B 1>/dev/null 2>/dev/null &) &
  echo "Fikkie daemon is running"
else
  celery -A fikkie.main worker -B
fi
