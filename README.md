# Backstage Code Challenge

Developed as part of the interview process with Backstage.

## Setup

* git clone git@github.com:zachcalvert/backstage_code_challenge.git
* cd backstage_code_challenge
* mkvirtualenv squares
* pip install -r requirements.txt
* echo "create database code_challenge" | mysql -u root -p  (empty password)
* ./manage.py migrate
* ./manage.py runserver
* navigate to 'http://localhost:8000/' in a web browser


### Requirements

* Develop a Django web service that can be queried at the following endpoint: localhost:8000/difference?number=n , where n is any integer greater than 0
and less than or equal to 100.

* Create a backbone application (or any other front end framework or just
jquery) based on the above backend service that should display a list of
the above values in the four columns described above.

* The web service should emit a JSON object of the following structure:
```
{
"datetime":current_datetime,
"value":solution,
"number":n,
"occurrences":occurrences // the number of times n has been requested
}

