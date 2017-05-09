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

## Flask REST

### api.py
-----
_**Description**_: We create an initial CreateUser API.         
*command*: python api.py
*client test*: curl -v -X POST  -H 'Content-Type: application/json' -d '{"email":"pauli@yahoo.es","password":"xxpassxx"}' http://localhost:5003/CreateUser    
*improvement*: 
