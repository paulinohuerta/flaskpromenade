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

# Scripts
-----

## Returning JSON format data

### hello.py
-----
_**Description**_: Adds a route to return JSON format data.      
*command*: python hello.py     
*URL 1*: http://localhost:5003/person/mary     
*URL 2*: http://localhost:5003/login?username=paolo&password=thehidden      
*URL 3*: http://localhost:5003/person/robert/age/36              
*URL 4*: curl -H 'Accept: application/json' -X GET http://localhost:5003/advices    
*improvement*: Moving the presentation logic into templates.    
