#!/bin/bash

source "./venv.sh"

echo "Creating machine (3)..."

cd machines
python main.py -c machine-3.json

