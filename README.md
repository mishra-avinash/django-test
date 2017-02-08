Setup
-----

1. Create a virtual environment and activate it in your shell:

        virtualenv -p /usr/bin/python3.4 env
        source ./env/bin/activate
    
2. Install required packages:

        pip install -r requirements.txt

3. Create the database and add a superuser:

        python manage.py migrate
        python manage.py createsuperuser
    
4. Start the development server and connect to http://127.0.0.1:8000/ in your browser:

        python manage.py runserver

Task
----

1. Set up the project on your machine (tested on Linux, macOS works as well, Windows might need extra work).
2. Add an `Employee` model to `rest_datagrid` app with an optional relationship to the default `User` model of Django, a full name, phone number, company, department, and occupation.
   Also add an admin interface for it.
3. Create an API with [Django REST framework](http://www.django-rest-framework.org/) (already installed, but not enabled or configured in `settings.py`) for authenticated
   users that shows and allows the creation of employees. Use a `ViewSet`, `Serializer` and the DRF router.
4. Set up a ReactJS application that consumes the API that you have created.
   * The application will have two separate routes:
     * The initial route (`/`) will query the endpoint, retrieve all employees and display the information in a table. The data should be automatically retrieved when the route is accessed .
     * The route (`/create/`) will prompt a form that allows the creation of employees and submits this information to the API.
   * Optional: Add authentication with JWT
5. Create unit tests for your model and a web testcase for your API.
6. Create a short screencast (i.e. http://screencast-o-matic.com/) that demos the admin interface,
   the API interface in the browser, and the datagrid. Please also walk us through your tests.
7. Send the results to codingtest@motius.de, include the following things:
  * Screencast
  * Code as `zip` file or on Github

Hints
-----

1. Django and React have a huge 3rd-party library of modules, make good use of them.
2. Keep an eye on active development of your 3rd party libraries, React and Django are frequently updated and sometimes break backwards compatibility with old code.
3. Make your project easy to set up and run. Update this README with installation and usage instructions.