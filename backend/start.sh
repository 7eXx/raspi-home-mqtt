#!/bin/bash

[ -f .env ] && . ./.env
[ -f .env.local ] && . ./.env.local

set -e

echo "Activating python virtual environment ..."
source ./venv/bin/activate

export GPIOZERO_PIN_FACTORY

echo "Starting backend ..."
python ./main.py