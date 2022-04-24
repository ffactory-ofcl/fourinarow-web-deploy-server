#! /bin/bash

git pull
[ ! -d "venv" ] && python3 -m venv venv
source venv/bin/activate
pip install git+https://github.com/dinvlad/python-github-webhook
pip install python-dotenv
python main.py