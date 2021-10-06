#!/bin/bash

source "./venv.sh"

echo "Creating machine (2)..."

cd machines
python main.py -c machine-2.json

