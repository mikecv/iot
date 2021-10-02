#!/bin/bash

source "./venv.sh"

echo "Creating proto files..."

cd controllers
python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/iot.proto
python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/ui.proto

cd ../machines
python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/iot.proto
