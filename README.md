

#Redd Manager
Please be sure to install the requirements in the requirments.txt fiel. Being able to work on python virtual environemtns is key as well for gunicorn to function.

###Django settings.py data setup
I do not keep the db server setup the django's settings.py needs on git since it contains password information but it looks a little something like this and connects to a local postgresql server. I've also included a copy of my nginx server config file

    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'john',
        'PASSWORD': 'reallyhardPWhere',
        'HOST': 'localhost',
        'PORT': '5432'
      }
    }


###Gunicorn instantion
This is how I spin up the Application instances. I have to be inside of the redd forlder containing the django application.

    gunicorn redd.wsgi:application --bind=127.0.0.1:9001
    gunicorn redd.wsgi:application --bind=127.0.0.1:7001

###Ember Front End
The front end is pretty simple. Just point nginx to the folder that contains the index.html file.

##Heads up

Be sure to change the logging file paths in the nginx settings files you use them. Also be sure to point the Djang servers in the .conf file at the proper directory.
