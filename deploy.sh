#! /bin/bash

cd /www/play.fourinarow.ffactory.me
git reset --hard @{u}
git clean -df
git pull -f
