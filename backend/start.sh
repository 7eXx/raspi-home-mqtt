#!/bin/bash

echo "Activating python virtual environment ..."
source ./venv/bin/activate

export GPIOZERO_PIN_FACTORY="mock"

echo "Starting backend ..."
python ./main.py