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

# Scripts
-----

## Models with SQLAlchemy

### The first model
-----
_**Description**_: We use the `MySQL driver` for this app, our database on the server is `usuario_db`, and we work on the `user table`, which is already created and stores some user data. SQLAlchemy must first be initialized with our app, will read our app's configuration and automatically connect to our database. We have created a `User model` to interact with a user table. We have also introduced as a new element in our study of the framework, a structure modular of our application, the users/run.py has the minimun code to start the app, while the users/my\_app/\_\_init\_\_.py contains the rest. Respecting this structure, soon, we will separate the models and views giving rise to new modules.     
*command*: python run.py       
*URL 1*: http://localhost:5300      
*improvement*: Templates and inheritance.     
