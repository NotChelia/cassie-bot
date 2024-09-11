#!/bin/sh
set -e


if [ "$DEBUG" = "true" ]; then
    echo "Running in debug mode with Python"
    python -m debugpy --listen 0.0.0.0:5678 --wait-for-client bot.py
else
    echo "Running in prod"
    python bot.py
fi
