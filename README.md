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

Task
----

1. Set up the project on MacOSX or Linux (on a virtual machine, if you are on Windows) according to the guide above.
2. Add an `Employee` model to `rest_datagrid` with an optional relationship to the `User` model, a full name, phone number, company, department, and occupation.
   Also add an admin interface for it.
3. Create an API with Django REST framework (already installed, but not configured in `settings.py`) for authenticated
   users that shows employees.
4. Use the DataTables plugin for jQuery to show a datagrid on the index page that uses the REST API you created.
5. Create a short screencast (i.e. http://screencast-o-matic.com/) that demos the admin interface,
   the API interface in the browser, and the datagrid.