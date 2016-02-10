Setup
-----

1. Create a virtual environment and activate it in your shell:

        virtualenv -p /usr/bin/python3.4 env
        source ./env/bin/activate
    
2. Install [Bower](http://bower.io/)

3. Install required packages:

        pip install -r requirements.txt
        bower update

4. Create the database and add a superuser:

        python manage.py migrate
        python manage.py createsuperuser
    
5. Copy the static files to the main folder `/static`:

        python manage.py collectstatic --noinput

6. Start the development server and connect to http://127.0.0.1:8000/ in your browser:

        python manage.py runserver

Task
----

1. Set up the project on MacOSX or Linux (on a virtual machine, if you are on Windows) according to the guide above.
2. Add an `Employee` model to `rest_datagrid` app with an optional relationship to the default `User` model of Django, a full name, phone number, company, department, and occupation.
   Also add an admin interface for it.
3. Create an API with [Django REST framework](http://www.django-rest-framework.org/) (already installed, but not enabled or configured in `settings.py`) for authenticated
   users that shows employees. Use a `ViewSet`, `Serializer` and the DRF router.
5. Use the DataTables plugin for jQuery to show a datagrid on the index page that uses the REST API you created. Use bower to install the latest stable release of DataTables. See `.bowerrc` for the installation path.
6. Create unit tests for your model and a web testcase for your API
7. Create a short screencast (i.e. http://screencast-o-matic.com/) that demos the admin interface,
   the API interface in the browser, and the datagrid.
8. Send the results via mail to philipp@motius.de - include the following things:
  * Screencast
  * Code as `zip` file or on Github