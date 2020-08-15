#!/usr/bin/env bash

# python 3.8
# python 버전 업그레이드: https://dlehdgml0480.tistory.com/8
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app.py
