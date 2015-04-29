Setup
-----

First create a virtual environment and activate it in your shell:

    virtualenv -p /usr/bin/python3.4 env
    source ./env/bin/activate
    
Install required packages, you might have to install bower first:

    pip install -r requirements.txt
    bower update

Create the database and add a superuser:

    python manage.py migrate
    python manage.py createsuperuser
    
Copy the static files to the main folder `/static`:

    python manage.py collectstatic --noinput

Start the development server and connect to http://127.0.0.1:8000/ in your browser:

    python manage.py runserver
