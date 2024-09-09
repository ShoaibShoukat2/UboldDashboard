

Getting Started
**********************


Django Setup
------------


1. Make sure to have `python3 <https://www.python.org/>`_, `pip3 <https://pip.pypa.io/en/stable/>`_ and `virtual environment <https://docs.python.org/3/library/venv.html>`_ installed on your system
2. Open the command line, create a new virtual environment and activate it
3. Install all the python dependencies, use the command: ::

    pip install -r requirements/local.txt
    
4. Create a new PostgreSQL database, use the command: ::
    
        createdb db_name
5. Copy the env.example and rename it to .env, you can replace the respected variables e.g. DATABASE_URL based on your configuration. You can refer to the `Django-cookiecutter <https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html>`_ project for more details.

6. Run the migration to sync the database, use the command: ::
    
        python manage.py migrate


-------------------------------------------

Frontend Setup
--------------
1. Make sure to have `node <https://nodejs.org/en/>`_ and `yarn <https://yarnpkg.com/>`_ installed on your system
2. Open the command line, install ``gulp`` globally, use the command: ::
    
        npm install -g gulp-cli
        npm install -g gulp
    
4. Install all the dependencies, use the command: ::
    
        yarn install

5. Now, you are ready to compile all the assets including scss, js and images, use the command: ::
    
        gulp

.. note:: This will compile all the static assets and watch out for any changes. If you would like to simply make production ready build, use the command ``gulp build``

