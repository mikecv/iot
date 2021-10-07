#!/bin/bash

source "./venv.sh"

echo "Creating machine (4)..."

cd machines
python main.py -c machine-4.json

