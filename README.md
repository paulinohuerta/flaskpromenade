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
_**Description**_: Moving the presentation logic into templates; We take advantage to introduce data acquisition from external sources, this time we get the members of a set structure of the server redis.     
*command*: python hello.py     
*URL*: http://localhost:5003/index    
*improvement*: Twitter Bootstrap integration mediante flask-bootstrap       
