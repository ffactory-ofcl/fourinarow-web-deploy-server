#! /bin/bash

[ ! -d "venv" ] && python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/dinvlad/python-github-webhook
python main.py