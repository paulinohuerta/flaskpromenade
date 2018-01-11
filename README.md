# flaskpromenade

## flask microframework introduction


### How to Work with the Code

    $ git clone https://github.com/paulinohuerta/flaskpromenade.git
    
The git clone command installs the source code from GitHub into a flaskpromenade folder. 

The commit history in this repository was carefully created to match the order in which concepts are presented.    
The recommended way to work with the code is to check out the commits starting from the oldest, then move forward through the commit list as you make progress.   

The Git command that lets you move through the change history is _git checkout_    

You can execute      

    $ git tag -l

and then,    

    $ git checkout 1a

Before you can check out a different revision, you will need to revert the files to their original state.         
The easiest way to do this is with the _git reset_ command     

    $ git reset --hard

#### Flask extensions or python packages that you should install

Well you should install using the pip command

    $ pip install <name_ext>

* redis
* flask
* flask-bootstrap
* flask-mysql
* flask-restful
* flask-wtf
* flask-moment
* flask-login
* flask-sqlalchemy
* flask-admin
* psycopg2

# Scripts
-----

## Using flask-admin

### Registering models with Flask-Admin
-----
_**Description**_: Flask-Admin extension was created to easily create administrator interfaces.     
Flask Admin works by registering view classes on the admin object that define one or more routes.     
We have imported ModelView from flask.ext.admin.contrib.sqla, which is provided by Flask-Admin to integrate SQLAlchemy models then, we have managed to create a simple interface "CRUD" that will allow the admin users to perform these operations on the records that other normal users generally can't.    
We should implement authentication as we did in a previous stage of our project through the extension `flask-login`.     
In short, in this application we have implemented admin views for our existing models with the facilities to perform CRUD operations.    
Additionally, we have added an own view, to do so we define a new class as a new view that inherits from `BaseView class`; after this, we will need to add this view to our admin object in the Flask configuration.    
In this example we do not need to customize the default behavior of Flask-Admin; for example, if we had created a user, we would be interested in hiding the user's password in the views.    
The database that stores our data is `postgresql`, then so we need the library `psycopg2` implemented in C as a `libpq` wrapper.    
*command*: python run.py       
*URL 1*: http://localhost:5300/admin     
*improvement*: Flask-Caching.    

