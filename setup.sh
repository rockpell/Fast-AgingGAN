#!/usr/bin/env bash

# python 3.8
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python3 app.py
