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

## Templates and inheritance

### Using Bootstrap framework, block composition and layout inheritance
-----
_**Description**_: To keep our templates DRY (Don't Repeat Yourself), we will use one of the most powerful features of Jinja, template inheritance.     
We need a basic HTML skeleton: `base.html`; The `block control` is used in inheritance to mark sections to be replaceable by the child template.     
The rest of the pages inherit from base.html. Then the `home page` template and `user.html` will use all the HTML base.html but replace the data in the `container block`.     
Template inheritance is when a child template can import a base template as a starting point and only replace marked sections in the base.    
In the code you will see that it has been commented as it would be the `SQLALCHEMY_DATABASE_URI` in the case that our data reside in a progresql database, in addition it is also commented in the model as it would be if the name of the class does not correspond with the name of the table, this is through `\_\_tablename\_\_`.    
`Jinja2` maintains a notion that the processing of logic should be handled in views and not in templates, and thus, it keeps the templates clean. We use a `context processor` to pass our values to a method; this will then be processed in a Python method, and our resultant value will be returned.     
*command*: python run.py       
*URL 1*: http://localhost:5300     
*improvement*: Completing the REST API, using SQLAlchemy for the model.    

