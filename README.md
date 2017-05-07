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

## Getting redis data

### hello.py
-----
_*Description**_: Flask-Bootstrap is initialized by passing the application instance in the constructor. The application extends a base template. Template inheritance allows you to build a base _skeleton_ template that contains all the common elements of your site.           
*command*: python hello.py     
*URL 1*: http://localhost:5003/index    
*URL 2*: http://localhost:5003/person/margaret           
*improvement*: getting data from MySQL server.       
