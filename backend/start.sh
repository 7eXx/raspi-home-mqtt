#!/bin/bash

[ -f .env ] && . ./.env
[ -f .env.local ] && . ./.env.local

set -e

echo "Activating python virtual environment ..."
source ./venv/bin/activate

export GPIOZERO_PIN_FACTORY=mock
export FLASK_APP=main.py
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0

echo "Starting backend ..."
flask run