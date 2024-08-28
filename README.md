# bankapi
Bank API using Django REST API

RUN
Setting up a new enviroment
python -m venv myappenv

Activate the Virtual Environment
source env/bin/activate

Then install dependencies
pip install Django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
pip install Django-rest-swagger

Run the app
cd Bank-api

Now we synced for the first time
python manage.py makemigrations
python manage.py migrate

And then Run the server
python manage.py runserver

