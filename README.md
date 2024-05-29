# In project directry start with: 
git clone https://github.com/krisvishwanathan/calendar.git

# Set up virtual environment
virtualenv env -> python -m venv .venv

source env/bin/activate -> .venv/Scripts/activate

deactivate

# Change directories to project folder
cd ./calendar

pip install -r requirements.txt

pip list

python3.10 manage.py makemigrations -> python manage.py makemigrations

python3.10 manage.py migrate -> python manage.py migrate

python3.10 manage.py runserver -> python manage.py runserver [can specify port if necessary]

access your site http://localhost:8000/ access the calendar

# Install/Uninstall project as a package
pip install .\dist\calendar-1.0-py3-none-any.whl

pip uninstall .\dist\calendar-1.0-py3-none-any.whl