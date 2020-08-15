#!/usr/bin/env bash

# python 3.8
# python 버전 업그레이드: https://dlehdgml0480.tistory.com/8
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# python 백그라운드 실행 및 종료: https://blkcoding.blogspot.com/2018/03/nohup.html
nohup python app.py > log.txt &
