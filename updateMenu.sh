#!/bin/sh
TODAY=date +%Y%m%d 
wget -x http://10.113.112.16:3002/todayFood -O todayFood.json
python3 updateMenu.py
git add *
git commit -m "`date +%Y%m%d` commit"
git push origin master
