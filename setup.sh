#!/usr/bin/env bash

# python 3.8
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app.py
