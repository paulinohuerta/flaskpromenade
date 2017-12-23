# flaskpromenade

## flask microframework introduction

# Scripts
-----

## Using URL built-in converters

### hello.py
-----
_**Description**_: A route to person/name. Other route to login with two HTTP GET parameters _username_ and _password_. Using [URL built-in converters](http://exploreflask.com/en/latest/views.html#url-converters).       
*command*: python hello.py     
*URL 1*: http://localhost:5003/person/mary     
*URL 2*: http://localhost:5003/login?username=paolo&password=thehidden      
*URL 3*: http://localhost:5003/person/robert/age/36              
*improvement*: returning JSON data.     
