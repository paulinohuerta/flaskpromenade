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


# Scripts
-----

## The first

### hello.py
-----
_**Description**_: Launches the flask integrated web server.     
*command*: python hello.py     
*URL*: http://localhost:5003/     
*improvement* getting a personalized salutation   

### hello.py
-----
_**Description**_: A route to person/name. Other route to login with two HTTP GET parameters _username_ and _password_       
*command*: python hello.py     
*URL 1*: http://localhost:5003/person/mary     
*URL 2*: http://localhost:5003/login?username=paolo&password=thehidden      
*improvement* using Flask’s built-in URL converters.     

### hello.py
-----
_**Description**_: A route to person/name. Other route to login with two HTTP GET parameters _username_ and _password_. Using [URL built-in converters](http://exploreflask.com/en/latest/views.html#url-converters).       
*command*: python hello.py     
*URL 1*: http://localhost:5003/person/mary     
*URL 2*: http://localhost:5003/login?username=paolo&password=thehidden      
*URL 3*: http://localhost:5003/person/robert/age/36              
*improvement* returning JSON data.     

### hello.py
-----
_**Description**_: Adds a route to return JSON format data.    
*command*: python hello.py     
*URL 1*: http://localhost:5003/person/mary     
*URL 2*: http://localhost:5003/login?username=paolo&password=thehidden      
*URL 3*: http://localhost:5003/person/robert/age/36              
*URL 4*: curl -H 'Accept: application/json' -X GET http://localhost:5003/advices

