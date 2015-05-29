# Backstage Code Challenge

Developed as part of the interview process with Backstage

## Setup

* git clone git@github.com:zachcalvert/backstage_code_challenge.git
* mkvirtualenv squares
* pip install -r requirements.txt
* echo "create database code_challenge" | mysql -u root -p  (empty password)
* ./manage.py migrate
* ./manage.py runserver
