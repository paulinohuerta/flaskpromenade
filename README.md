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

## Flask WTF

### hello.py
-----
_**Description**_: Flask-Bootstrap provides a higth-level of funcionality that renders an entire "Flask-WTF form". When importing *bootstrap/wtf.html* file are defined template elements  and helper functions such as wtf.quick\_form() function, this function takes a flask-wtf object and renders it using default Bootstrp styles.     
Note: This example is based on the example used by Miguel Grinberg in his book "Flask Web development" published by O'Reilly Publishing.   
*command*: python hello.py       
*URL*: http://localhost:5003/        
*improvement*:
