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

## REST API interface (using SQLAlchemy for the model)

### Completing the API of a previous chapter
-----
_**Description**_: We use the `MySQL driver` for this app, our database on the server is `catalog_db`, and we work on the `product table` and `category table`, which are already created and stores some data.      
We use `Blueprints` in order to distribute the code in different files, considering then, that our application will consist of several modules.      
We use SQLAlchemy fas an `ORM` of our relational model; we want to have product categories where each category can have multiple products, but each product should have at least one category.    
See below the mapping according to "REST" that we propose in our interface.    
Our API is inside the views.py, there you find code commented on each of the methods; it is interesting, initially to test the application only with that code, for example that the `get function` only had the line of code `return 'This is a GET response'`.        
*command*: python run.py       
*URL 1*: http://localhost:5300/api             
*Mapping our API*:       
GET /api/products/1 : This gets the product with ID 1      
GET /api/products : This gets the list of products      
POST /api/products : This creates a new product     
PUT /api/products/1 : This updates the product with ID 1     
DELETE /api/products/1 : This deletes the product with ID 1     
*improvement*: Using flask-admin.     
