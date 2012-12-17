Presuming debian based distro:

sudo apt-get install python-pip python-virtualenv  libpq-dev python-dev (required for psycopg2) 

virtualenv --no-site-packages venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver
