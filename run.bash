#!/usr/bin/env bash

PATH=${PATH}:/usr/local/bin

pip3.8 install -r requirements.txt

docker-compose up -d

PYTHONPATH=. python3.8 -m pytest