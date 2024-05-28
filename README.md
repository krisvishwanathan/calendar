In project directry start with:
git clone https://github.com/krisvishwanathan/calendar.git

virtualenv env

source env/bin/activate

pip install -requirements

python3.10 manage.py makemigrations

python3.10 manage.py migrate

python3.10 manage.py runserver

access your site http://localhost:8000/ access the calendar
